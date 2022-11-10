import socket

HOST = 'localhost'
PORT = 64000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    response = 'Y'
    data_to_send = "Echo!!!!"

    while response == 'Y':
        sock.sendall(data_to_send.encode())
        data = sock.recv(512)
        print('Received', repr(data))
        response = input("Send again (Y/N)? ")
        if response == 'Y':
            data_to_send = input("Enter data: ")

    print("Goodbye!")
