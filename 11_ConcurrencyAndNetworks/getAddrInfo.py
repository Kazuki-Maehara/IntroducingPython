import socket


print(socket.getaddrinfo('DOMAIN_NAME_TO_A_WEBSITE', 80))
print(socket.getaddrinfo('DOMAIN_NAME_TO_A_WEBSITE',
                         80, socket.AF_INET, socket.SOCK_STREAM))
