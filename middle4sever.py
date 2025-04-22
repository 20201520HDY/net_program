import socket
from datetime import datetime

HOST = '127.0.0.1'
PORT1 = 9999
PORT2 = 9002

def get_time():
    return datetime.now().strftime('%a %b %d %H:%M:%S %Y')

def request_data(device_number):
    if device_number == '1':
        port = PORT1
        label = 'Device1'
    else:
        port = PORT2
        label = 'Device2'

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, port))
        count = 0
        with open('data.txt', 'a') as f:
            while count < 5:
                s.sendall('Request'.encode())
                data = s.recv(1024).decode()
                line = f"{get_time()}: {label}: {data}\n"
                f.write(line)
                count += 1
        s.sendall('quit'.encode())

while True:
    cmd = input("Enter 1 or 2 to collect from device, or 'quit' to exit: ")
    if cmd == '1' or cmd == '2':
        request_data(cmd)
    elif cmd == 'quit':
        for p in [PORT1, PORT2]:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, p))
                s.sendall('quit'.encode())
        break