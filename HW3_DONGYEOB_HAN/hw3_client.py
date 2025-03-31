import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

# 서버의 인사 메시지 수신 후 출력
msg = sock.recv(1024)
print(msg.decode())

# 본인의 이름을 서버로 전송
my_name = '한동엽'
sock.send(my_name.encode())

# 서버로부터 학번(4바이트)을 수신 후 엔디언 변환하여 출력
data = sock.recv(4)
student_id = int.from_bytes(data, 'big')
print(student_id)

sock.close()