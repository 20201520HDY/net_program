import socket
import struct  # 엔디언 변환을 위한 모듈

# 서버 소켓 설정
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)

    # 클라이언트로부터 이름 수신
    name = client.recv(1024).decode()
    print(f"Student Name: {name}")

    # 클라이언트로부터 학번 수신
    student_id_bytes = client.recv(4)  # 학번은 4바이트 정수
    student_id = struct.unpack("<I", student_id_bytes)[0]  # 엔디언 변환 후 정수로 변환
    print(f"Student ID: {student_id}")

    # 클라이언트에게 응답
    client.send(f"Hello {name}, your student ID is {student_id}".encode())

    client.close()
