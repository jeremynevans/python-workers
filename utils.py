import requests, os
import redis

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis_conn = redis.from_url(redis_url)

def greet(data: dict):
  greeting = 'Hello, ' + data.get('name')
  key = data.get('key')
  redis_conn.set(key, greeting)
