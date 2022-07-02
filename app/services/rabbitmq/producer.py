import os
import string
from app.services.rabbitmq.schemas import RabbitBody
import aiormq

exchange_name = os.environ.get("EXCHANGE_NAME")
queue_name = os.environ.get("QUEUE_NAME")
routing_key = os.environ.get("ROUTING_KEY")
rabbitmq_host = os.environ.get("RABBITMQ_HOST")
rabbitmq_user = os.environ.get("RABBITMQ_USER")
rabbitmq_password = os.environ.get("RABBITMQ_PASSWORD")

# Para criar e rodar um servidor rabbitmq de maneira simples, sugiro o seguinte comando docker:
# sudo docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.10-management


async def push_to_queue(message: string):
    request = RabbitBody(message)

    connection = await aiormq.connect("amqp://{}:{}@{}/".format(rabbitmq_user, rabbitmq_password, rabbitmq_host))
    channel = await connection.channel()

    await channel.exchange_declare(
        exchange=exchange_name, exchange_type='direct'
    )

    await channel.queue_declare(
        queue=queue_name)

    await channel.queue_bind(
        queue=queue_name,
        exchange=exchange_name,
        routing_key=routing_key)

    await channel.basic_publish(
        body=request.encode(),
        routing_key=routing_key,
        exchange=exchange_name,
    )
