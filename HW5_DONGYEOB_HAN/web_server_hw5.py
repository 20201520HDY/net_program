
from socket import *

# MIME 타입 정의
mime_types = {
    'html': 'text/html',
    'png': 'image/png',
    'ico': 'image/x-icon'
}

# 서버 설정
s = socket()
s.bind(('', 80))
s.listen(10)

print("웹 서버가 실행 중입니다...")

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    
    if len(req) > 0:
        first_line = req[0]  # GET /index.html HTTP/1.1
        parts = first_line.split(' ')
        if len(parts) > 1:
            filename = parts[1].lstrip('/')
            if filename == '':
                filename = 'index.html'

            try:
                ext = filename.split('.')[-1]
                mimeType = mime_types.get(ext, 'application/octet-stream')
                
                if ext == 'html':
                    f = open(filename, 'r', encoding='utf-8')
                    data = f.read()
                    f.close()
                    c.send(b'HTTP/1.1 200 OK\r\n')
                    c.send(f'Content-Type: {mimeType}\r\n\r\n'.encode())
                    c.send(data.encode('euc-kr'))
                else:
                    f = open(filename, 'rb')
                    data = f.read()
                    f.close()
                    c.send(b'HTTP/1.1 200 OK\r\n')
                    c.send(f'Content-Type: {mimeType}\r\n\r\n'.encode())
                    c.send(data)
            except:
                c.send(b'HTTP/1.1 404 Not Found\r\n\r\n')
                c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
                c.send(b'<BODY>Not Found</BODY></HTML>')

    c.close()
