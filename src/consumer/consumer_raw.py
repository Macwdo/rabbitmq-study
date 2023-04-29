import pika

def my_cb(ch, method, properties, body):
    print(body)

connection_parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

channel = pika.BlockingConnection(connection_parameters).channel()

channel.queue_declare(
    queue="my_new_queue",
    durable=True
)

channel.basic_consume(
    queue="my_new_queue",
    auto_ack=True,
    on_message_callback=my_cb
)

print(f"Listen RMQ on 5762")
channel.start_consuming()