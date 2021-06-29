snowman = '\u2603'

print(len(snowman))

ds = snowman.encode('utf-8')
print(ds)

ds = snowman.encode('ascii', 'ignore')
# da = snowman.encode('ascii')
print(ds)

ds = snowman.encode('ascii', 'replace')
print(ds)

ds = snowman.encode('ascii', 'backslashreplace')
print(ds)

ds = snowman.encode('ascii', 'xmlcharrefreplace')
print(ds)
