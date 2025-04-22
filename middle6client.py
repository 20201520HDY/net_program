def tcp_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 5050))
    while True:
        msg = input('> ')
        s.send(msg.encode())
        data = s.recv(1024)
        print('Server:', data.decode())
        if msg == "quit":
            break
    s.close()