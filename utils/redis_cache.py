import redis
import os

redis_client = redis.from_url(os.getenv("REDIS_URL"))

def set_cache(key, value):

    redis_client.set(key, value)

def get_cache(key):

    return redis_client.get(key)

def delete_cache(key):

    redis_client.delete(key)
