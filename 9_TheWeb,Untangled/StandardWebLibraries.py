import urllib.request
sp = 30

url = 'URL_TO_API'
conn = urllib.request.urlopen(url)

print(conn)

data = conn.read()
print(data)

print('-' * sp)
print(conn.status)
print('-' * sp)

print(conn.getheader('Content-Type'))
print('-' * sp)

for key, value in conn.getheaders():
    print(key, value)
