import socket

HOST = '127.0.0.1'
PORT = 9000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print("서버 실행 중...")

conn, addr = server_socket.accept()
print('클라이언트 연결됨:', addr)

while True:
    data = conn.recv(1024).decode()
    if data.lower() == 'q':
        print('클라이언트 종료')
        break

    try:
        num1, op, num2 = data.split()
        num1, num2 = float(num1), float(num2)
        result = 0

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = round(num1 / num2, 1)

        conn.send(str(result).encode())

    except Exception as e:
        conn.send(f"에러: {e}".encode())

conn.close()
server_socket.close()
