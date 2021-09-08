import redis
import time


conn = redis.Redis('localhost', 6379)
key = 'now you see it'

print(conn.set(key, 'but not for long'))

print(conn.expire(key, 3))

print(conn.ttl(key))

print(conn.get(key))

time.sleep(4)

conn.get(key)

print('conn.get(key) was invoked.')
