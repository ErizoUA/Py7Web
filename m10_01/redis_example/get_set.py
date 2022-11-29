import redis

client = redis.Redis(host='localhost', port=6379, password=None)

if __name__ == '__main__':
    client.set('name', 'Alexey')
    client.set('age', 23)

    print(client.get('name').decode())
    print(int(client.get('age').decode()))
