#!/usr/bin/env python
import pika

from datetime import datetime
import sys
import json

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='task_mock', exchange_type='direct')
channel.queue_declare(queue='task_queue', durable=True)
channel.queue_declare(queue='hello')
channel.queue_bind(exchange='task_mock', queue='task_queue')
channel.queue_bind(exchange='task_mock', queue='hello')

if __name__ == '__main__':

    for i in range(5):
        message = {
            "id": i,
            "payload": f"Task #{i}",
            "date": datetime.now().isoformat()
        }

        channel.basic_publish(
            exchange='task_mock',
            routing_key='task_queue',
            body=json.dumps(message).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
        print(" [x] Sent %r" % message)
    channel.basic_publish(exchange='task_mock', routing_key='hello', body='Completed tasks'.encode())
    connection.close()
