import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from', addr)

    # 클라이언트에게 인사 메시지 전송
    client.send(b'Hello ' + addr[0].encode())

    # 클라이언트에서 보낸 이름 수신 후 출력
    name = client.recv(1024).decode()
    print(name)

    # 학생의 학번(정수형)을 엔디언 변환하여 전송 (문자열 변환 금지)
    student_id = 20201520
    client.send(student_id.to_bytes(4, 'big'))

    client.close()