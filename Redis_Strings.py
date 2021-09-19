import redis


conn = redis.Redis('localhost', 6379)
conn.keys('*')

conn.set('secret', 'ni!')
conn.set('carats', 24)
conn.set('fever', 101.5)

print(conn.get('secret'))
print(conn.get('carats'))
print(conn.get('fever'))

conn.setnx('secret', 'icky-icky-icky-ptang-zoop-boing!')
print(conn.get('secret'))

print(conn.getset('secret', 'icky-icky-icky-ptang-zoop-boing!'))

print(conn.get('secret'))

print(conn.getrange('secret', -6, -1))

print(conn.setrange('secret', 0, 'ICKY'))

print(conn.get('secret'))

conn.mset({'pie': 'cherry', 'cordial': 'sherry'})
print(conn.mget(['pie', 'cordial']))

print(conn.delete('pie'))

print(conn.incr('carats'))

print(conn.incr('carats', 10))

print(conn.decr('carats'))

print(conn.decr('carats', 15))

print(conn.incrbyfloat('fever'))

print(conn.incrbyfloat('fever', 0.5))

print(conn.incrbyfloat('fever', -2.0))
