import socket

PORT = 2500
BUFFER = 1024

s = socket.socket()
s.connect(('localhost', PORT))

while True:
    msg = input('Message to send: ')
    if msg.lower() == 'quit':
        break
    s.send(msg.encode())
    data = s.recv(BUFFER)
    print('Received message:', data.decode())

s.close()
