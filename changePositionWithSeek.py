import os

fin = open('bfile', 'rb')
print(fin.tell())

print(fin.seek(255))

bdata = fin.read()
print(len(bdata))
print(bdata[0])

print(os.SEEK_SET)
print(os.SEEK_CUR)
print(os.SEEK_END)

print(fin.seek(-2, 2))
print(fin.tell())

bdata = fin.read()
print(len(bdata))
print(bdata[0])

fin.seek(254, 0)
print(fin.tell())

fin.seek(1, 1)
print(fin.tell())

bdata = fin.read()
print(len(bdata))
print(bdata[0])
