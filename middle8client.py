import time

def udp_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(1)
    msg = input("Enter message: ").encode()
    retries = 0
    while retries < 4:
        s.sendto(msg, ('localhost', 6789))
        try:
            data, _ = s.recvfrom(1024)
            print("Server says:", data.decode())
            break
        except socket.timeout:
            retries += 1
            print(f"Timeout... retrying ({retries})")
    if retries == 4:
        print("Failed to get ack after 4 attempts")
    s.close()