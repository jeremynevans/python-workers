import requests, os, random, redis
from rq import Queue
from worker import redis_conn
from utils import greet
from flask import Flask, jsonify, request

q = Queue(connection=redis_conn)

app = Flask(__name__)

@app.route('/submit', methods=['GET'])
def submit():
  name = request.args.get('name')
  key = random.randint(1, 1000000000000)
  data = {
    'name': name,
    'key': key
  }
  queued_task = q.enqueue(greet, data)
  print(queued_task.key)
  return 'key: ' + str(key)

@app.route('/progress', methods=['GET'])
def progress():
  key = request.args.get('key')
  value = redis_conn.get(key)
  return value if value else 'None'



if __name__ == '__main__':
  # Bind to PORT if defined, otherwise default to 5000.
  port = int(os.environ.get('PORT', 5050))
  app.run(host='0.0.0.0', port=port)
