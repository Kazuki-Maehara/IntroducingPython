bdata = bytes(range(0, 256))
print(len(bdata))

fout = open('bfile', 'wb')
print(fout.write(bdata))

fout.close()
