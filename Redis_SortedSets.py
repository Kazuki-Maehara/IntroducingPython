import redis
import time


now = time.time()

conn = redis.Redis('localhost', 6379)
conn.flushall()

print(conn.zadd('logins', {'smeagol': now}))

print(conn.zadd('logins', {'sauron': now+(5*60)}))

print(conn.zadd('logins', {'bilbo': now+(2*60*60)}))

print(conn.zadd('logins', {'treebeard': now+(24*60*60)}))

print(conn.zrank('logins', 'bilbo'))

print(conn.zscore('logins', 'bilbo'))

print(conn.zrange('logins', 0, -1))

print(conn.zrange('logins', 0, -1, withscores=True))
