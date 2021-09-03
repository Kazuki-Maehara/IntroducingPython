import redis


conn = redis.Redis('localhost', 6379)
conn.flushall()

days = ['2021-08-11', '2021-08-12', '2021-08-13']
big_spender = 1089
tire_kicker = 40459
late_joiner = 550212

print(conn.setbit(days[0], big_spender, 1))
print(conn.setbit(days[0], tire_kicker, 1))

print(conn.setbit(days[1], big_spender, 1))

print(conn.setbit(days[2], big_spender, 1))
print(conn.setbit(days[2], late_joiner, 1))

for day in days:
    print(day, ": ", conn.bitcount(day))

print(conn.getbit(days[1], tire_kicker))

print(conn.bitop('and', 'everyday', *days))

print(conn.bitcount('everyday'))

print(conn.getbit('everyday', big_spender))

print(conn.bitop('or', 'alldays', *days))

print(conn.bitcount('alldays'))
