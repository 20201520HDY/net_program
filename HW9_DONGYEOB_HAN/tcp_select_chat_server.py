import socket
import select

PORT = 2500
BUFFER = 1024
socks = []  # 소켓 리스트

# 서버 소켓 생성 및 리스닝
s_sock = socket.socket()
s_sock.bind(('', PORT))
s_sock.listen(5)

socks.append(s_sock)
print(f'{PORT}에서 접속 대기 중')

while True:
    r_sock, _, _ = select.select(socks, [], [])

    for s in r_sock:
        # 새 클라이언트 접속
        if s == s_sock:
            c_sock, addr = s_sock.accept()
            socks.append(c_sock)
            print(f'Client {addr} connected')
        else:
            # 기존 클라이언트로부터 메시지 수신
            data = s.recv(BUFFER)
            if not data:
                s.close()
                socks.remove(s)
                continue

            print("Received:", data.decode())
            s.send(data)  # 받은 메시지를 다시 클라이언트에 전송
