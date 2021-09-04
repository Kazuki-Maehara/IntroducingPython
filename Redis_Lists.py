import redis


conn = redis.Redis('localhost', 6379)
conn.flushall()

print(conn.lpush('zoo', 'bear'))
print(conn.lindex('zoo', 0))

print(conn.lpush('zoo', 'alligator', 'duck'))
print(conn.lrange('zoo', 0, -1))

print(conn.linsert('zoo', 'before', 'bear', 'beaver'))
print(conn.lrange('zoo', 0, -1))

print(conn.linsert('zoo', 'after', 'bear', 'cassowary'))
print(conn.lrange('zoo', 0, -1))

print(conn.lset('zoo', 2, 'marmoset'))
print(conn.lrange('zoo', 0, -1))

print(conn.rpush('zoo', 'yak'))
print(conn.lrange('zoo', 0, -1))

print(conn.lrange('zoo', 0, 2))

print(conn.ltrim('zoo', 1, 4))
print(conn.lrange('zoo', 0, -1))
