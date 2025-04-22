from socket import *
import random

port = 7000
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    # 클라이언트 메시지 수신
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)

        if random.random() <= 0.5:
            continue  # ack 손실 시뮬레이션
        else:
            sock.sendto(b'ack', addr)
            print('<-', data.decode())
            break

    # 서버 사용자 응답 입력 후 전송
    msg = input('-> ')
    sock.sendto(msg.encode(), addr)
