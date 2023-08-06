import asyncio
import functools
from abc import ABC
from asyncio import Task

import aio_pika.queue
import loguru
import ujson
from aio_pika import connect_robust, RobustConnection, Message
from aio_pika.abc import AbstractChannel, AbstractIncomingMessage, ExchangeType
from aiormq import DuplicateConsumerTag


class Consumer:
    def __init__(self, queue, receiver, consumer_tag):
        self.queue: aio_pika.queue.Queue = queue
        self.receiver = receiver
        self.consumer_tag = consumer_tag

    async def start(self):
        await self.queue.consume(self.receiver, consumer_tag=self.consumer_tag)

    async def stop(self):
        await self.queue.cancel(self.consumer_tag, timeout=5)
        try:
            loguru.logger.debug(self.queue.channel.consumers)
            # self.queue.channel.consumers.pop(self.consumer_tag)
        except KeyError as e:
            loguru.logger.error(f'KeyError: {e}')

    def __str__(self):
        return f'<Consumer: {self.consumer_tag}>'

    def __repr__(self):
        return self.__str__()


class Eventory:
    def __init__(self, amqp_url):
        self.url = amqp_url
        self._connection: RobustConnection | None = None
        self._channels: dict[str, AbstractChannel] = {}
        self._listener_task: Task | None = None
        self._consumers = []

    async def connect(self):
        self._connection = await connect_robust(self.url)

    async def close(self):
        await self._connection.close()

    async def reconnect(self):
        await self._connection.reconnect()

    async def get_channel(self, app_name):
        if app_name not in self._channels:
            self._channels[app_name] = await self._connection.channel()

        return self._channels[app_name]

    async def register_consumer(self, app_name, routing_key, callback, *args, **kwargs):
        channel = await self.get_channel(app_name)
        exchange = await channel.declare_exchange(routing_key, type=ExchangeType.FANOUT, auto_delete=True)
        queue = await channel.declare_queue(exclusive=True)
        await queue.bind(exchange)

        try:
            receiver = self._on_message_wrapper(callback, *args, **kwargs)
            consumer = Consumer(queue, receiver, callback.__name__)
            return consumer
        except DuplicateConsumerTag:
            raise RuntimeError(f'Duplicated consumer_tag: "{callback.__name__}"')

    async def publish(self, obj, routing_key, app_name):
        message = Message(
            body=ujson.dumps(obj, ensure_ascii=False).encode('utf-8'),
            content_type='application/json',
            content_encoding='utf-8'
        )
        channel = await self.get_channel(app_name)
        exchange = await channel.declare_exchange(routing_key, type=ExchangeType.FANOUT, auto_delete=True)
        return await exchange.publish(
            message=message,
            routing_key=routing_key
        )

    def consumer(self, routing_key: str):
        def wrap(coro):
            self._consumers.append((coro, routing_key))
        return wrap

    def start_listening(self):
        for callback, routing_key in self._consumers:
            asyncio.create_task(self.register_consumer('<NOT_APP>', routing_key, callback))

        self._listener_task = asyncio.ensure_future(asyncio.Future())

    def stop_listening(self):
        if self._listener_task:
            self._listener_task.cancel()

    def restart_listening(self):
        self.stop_listening()
        self.start_listening()

    @staticmethod
    def _on_message_wrapper(coro, *args, **kwargs):
        @functools.wraps(coro)
        async def _receive(message: AbstractIncomingMessage):
            async with message.process():
                loguru.logger.debug(
                    f'Received message; consumer_tag={message.consumer_tag}  exchange={message.exchange}')
                message.json = ujson.loads(message.body.decode('utf-8'))
                return await coro(message, *args, **kwargs)

        return _receive


class JSONMessage(AbstractIncomingMessage, ABC):
    json: dict
