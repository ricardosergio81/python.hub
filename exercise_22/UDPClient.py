import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = 'localhost'
port = 5432

message = 'Hello server'
try:
    s.sendto(message.encode(), (host, port))
    dados, server = s.recvfrom(4096)
    dados = dados.decode()
    print(f"{dados}")
finally:
    s.close()
