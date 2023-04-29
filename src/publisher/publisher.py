import pika
import json


class RabbitMQPublisher:
    def __init__(self) -> None:
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__queue = "my_new_queue"
        self.__channel = self.__create_channel()


    def __create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host="localhost",
            port=5672,
            credentials=pika.PlainCredentials(
                username="guest",
                password="guest"
            )
        )

        channel = pika.BlockingConnection(connection_parameters).channel()
        return channel
    

    def publish(self, body: dict):
        self.__channel.basic_publish(
            exchange="my_new_exchange",
            routing_key="",
            body= json.dumps(body),
            properties=pika.BasicProperties(
            delivery_mode=2
            )
        )

publisher = RabbitMQPublisher()

publisher.publish({"algo": "assim"})
