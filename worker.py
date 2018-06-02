import os
import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
print('redis_url: ' + redis_url)

redis_conn = redis.from_url(redis_url)

if __name__ == '__main__':
  print("HI")
  with Connection(redis_conn):
    worker = Worker(map(Queue, listen))
    worker.work()
