import string
import re

printable = string.printable
print(len(printable))
half = int(len(printable)/2)

print(printable[0:half])

print(printable[half:])

m = re.findall('\d', printable)
print(m)

m = re.findall('\s', printable)
print(m)

x = 'abc' + '-/*' + '\u00ea' + '\u0115'
m = re.findall('\w', x)
print(m)
