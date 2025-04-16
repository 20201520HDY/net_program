from socket import *
import threading

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
server_addr = ('localhost', port)
sock.settimeout(2)

# ack 수신 여부를 공유하기 위한 이벤트 객체
ack_event = threading.Event()

def receive_thread():
    while True:
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
            decoded = data.decode()
            # 만약 받은 메시지가 "ack"이면 이벤트를 설정
            if decoded == 'ack':
                ack_event.set()
            else:
                # ack가 아닌 응답은 바로 화면에 출력
                print("<-", decoded)
        except Exception:
            continue

def input_thread():
    while True:
        # 사용자 입력 (화면에는 "-> "만 보임)
        msg = input("-> ")
        # 새 메시지 전송 전에 ack 이벤트 초기화
        ack_event.clear()
        reTx = 0
        
        # 최대 5회까지 재전송 시도
        while reTx <= 5:
            full_msg = f"{reTx} {msg}"
            # 재전송 횟수가 포함된 메시지를 출력 (예: "-> 0 Hello")
            print("->", full_msg)
            sock.sendto(full_msg.encode(), server_addr)
            
            # 최대 2초간 ack를 기다림
            if ack_event.wait(timeout=2):
                break
            else:
                reTx += 1
        
        # 만약 ack를 받지 못했으면 사용자에게 알려주지만, 이후 바로 다음 메시지 입력으로 넘어감
        if not ack_event.is_set():
            print("<- (서버 응답 없음)")

# 수신 쓰레드를 데몬으로 실행
threading.Thread(target=receive_thread, daemon=True).start()
# 메인 쓰레드는 입력 처리 전용
input_thread()
