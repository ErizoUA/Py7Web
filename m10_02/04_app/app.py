#!/usr/bin/env python
import pika
from faker import Faker

from datetime import datetime
import sys
import json

from models import Contact

faker = Faker()

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='mail_service', exchange_type='direct')
channel.queue_declare(queue='marketing_campaign', durable=True)
channel.queue_bind(exchange='mail_service', queue='marketing_campaign')


def main():
    for i in range(5):
        contact = Contact(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.ascii_free_email()
        ).save()

        channel.basic_publish(
            exchange='mail_service',
            routing_key='marketing_campaign',
            body=str(contact.id).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))

    connection.close()


if __name__ == '__main__':
    main()

