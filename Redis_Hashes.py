import redis


conn = redis.Redis('localhost', 6379)
conn.flushall()

print(conn.hmset('song', {'do': 'a deer', 're': 'about a deer'}))
print(conn.hgetall('song'))

print(conn.hset('song', 'mi', 'a note to follow re'))
print(conn.hgetall('song'))

print(conn.hget('song', 'mi'))

print(conn.hmget('song', 're', 'do'))

print(conn.hkeys('song'))

print(conn.hvals('song'))

print(conn.hlen('song'))

print(conn.hsetnx('song', 'fa', 'a note that rhymes with la'))
print(conn.hgetall('song'))
