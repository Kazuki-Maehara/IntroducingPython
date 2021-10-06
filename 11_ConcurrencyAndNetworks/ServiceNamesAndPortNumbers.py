import socket


print(socket.getservbyname('http'))
print(socket.getservbyport(80))
print(socket.getservbyname('smtp'))
print(socket.getservbyport(25))
