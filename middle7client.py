import socket
import random

HOST = '127.0.0.1'
PORT = 9001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Device1 waiting for connection...')
    conn, addr = s.accept()
    with conn:
        print(f'Connected by {addr}')
        while True:
            data = conn.recv(1024).decode()
            if data == 'Request':
                temp = random.randint(0, 40)
                humid = random.randint(0, 100)
                ilium = random.randint(70, 150)
                msg = f"Temp={temp}, Humid={humid}, Ilium={ilium}"
                conn.sendall(msg.encode())
            elif data == 'quit':
                break
