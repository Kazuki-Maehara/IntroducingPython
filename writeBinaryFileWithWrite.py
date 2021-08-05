bdata = bytes(range(0, 256))
print(len(bdata))

fout = open('bfile', 'wb')
result = fout.write(bdata)
print(result, '-byte data is written')
fout.close()
