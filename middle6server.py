import socket
import threading

mailbox = {}

def handle_client(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        msg = data.decode()
        if msg.startswith("send"):
            _, mboxID, *message = msg.split()
            message = ' '.join(message)
            mailbox.setdefault(mboxID, []).append(message)
            conn.send(b"OK")
        elif msg.startswith("receive"):
            _, mboxID = msg.split()
            if mboxID in mailbox and mailbox[mboxID]:
                conn.send(mailbox[mboxID].pop(0).encode())
            else:
                conn.send(b"No messages")
        elif msg == "quit":
            conn.send(b"Bye")
            break
    conn.close()

def tcp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 5050))
    s.listen(5)
    print('Server started')
    while True:
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        threading.Thread(target=handle_client, args=(conn,)).start()
