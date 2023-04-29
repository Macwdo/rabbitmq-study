import pika


connection_parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

channel = pika.BlockingConnection(connection_parameters).channel()

channel.basic_publish(
    exchange="my_new_exchange",
    routing_key="",
    body=f"Algo",
    properties=pika.BasicProperties(
    delivery_mode=2
    )
)