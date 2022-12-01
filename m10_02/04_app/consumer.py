#!/usr/bin/env python
import pika

import time
import json

from models import Contact
from email_service import send_email


def callback(ch, method, properties, body):
    id_ = body.decode()
    query_contact = Contact.objects(id=id_, completed=False)
    contact, *rest = query_contact
    if contact:
        email = contact.email
        fullname = f'{contact.first_name} {contact.last_name}'
        send_email('info@roga_copyta.com.ua', email, f'Hello {fullname}')
        query_contact.update_one(set__completed=True)
    ch.basic_ack(delivery_tag=method.delivery_tag)


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='marketing_campaign', durable=True)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='marketing_campaign', on_message_callback=callback)


if __name__ == '__main__':
    channel.start_consuming()
