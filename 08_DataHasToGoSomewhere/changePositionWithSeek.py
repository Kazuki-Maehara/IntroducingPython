import os
fin = open('bfile', 'rb')
print(fin.tell())

print(fin.seek(254))
bdata = fin.read()
print(len(bdata))
print(bdata[0], bdata[1])

print(os.SEEK_SET, os.SEEK_CUR, os.SEEK_END)

fin.seek(-1, os.SEEK_END)
print(fin.tell())

bdata = fin.read()
print(len(bdata))

print(bdata[0])

fin = open('bfile', 'rb')
fin.seek(254, os.SEEK_SET)
print(fin.tell())
fin.seek(1, os.SEEK_CUR)
print(fin.tell())
bdata = fin.read()
print(len(bdata))
print(bdata[0])
