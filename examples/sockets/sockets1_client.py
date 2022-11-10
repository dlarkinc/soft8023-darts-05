import socket

HOST = 'localhost'
PORT = 64000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(b'Echo!!!!')
    data = sock.recv(512)
    sock.close()

print('Received', repr(data))
