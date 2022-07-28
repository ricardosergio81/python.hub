import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = 'localhost'
port = 5432

s.bind((host, port))
message = ' Hello client'
while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        s.sendto(dados + (message.encode()), end)
