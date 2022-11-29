import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client, default_ttl=1, max_size=100000)


@cache
def f(x):
    print(f"Виклик функції f({x})")
    return x


if __name__ == '__main__':
    f(3)
    f(3)
