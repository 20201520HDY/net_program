import socket

HOST = '127.0.0.1'
PORT = 9000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    expr = input("계산식 입력 (예: 20 + 17, 종료: q): ")
    client_socket.send(expr.encode())

    if expr.lower() == 'q':
        break

    result = client_socket.recv(1024).decode()
    print("결과:", result)

client_socket.close()
