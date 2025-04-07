import socket
import random

HOST = '127.0.0.1'
PORT = 9002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Device2 waiting for connection...')
    conn, addr = s.accept()
    with conn:
        print(f'Connected by {addr}')
        while True:
            data = conn.recv(1024).decode()
            if data == 'Request':
                heartbeat = random.randint(40, 140)
                steps = random.randint(2000, 6000)
                cal = random.randint(1000, 4000)
                msg = f"Heartbeat={heartbeat}, Steps={steps}, Cal={cal}"
                conn.sendall(msg.encode())
            elif data == 'quit':
                break
