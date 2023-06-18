import socket
import display
import time

global receiver_ip, receiver_port, sock, packs, frame_count, frame_received, start_time

receiver_ip = socket.gethostname()
receiver_port = 4000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1/10)

packs = []
order = []
frame_received = False

# Initialize the FPS counter
frame_count = 0
start_time = time.time() + 1

def check_differences(array):
    if len(array) < 2:
        return None
    for i in range (0,len(array)):
        array[i] = array[i] * len(array)
    temp = float(array[1]) - float(array[0]) 
    for i in range(0,len(array) - 1):
        if temp != float(array[i+1]) - float(array[i]):
            return None
    return True


def main():
    global receiver_ip, receiver_port, sock, packs, frame_count, frame_received, start_time, sock, order
    try:
        sock.bind((receiver_ip, receiver_port))
    except:
        pass
    if start_time < time.time():
        start_time = time.time() + 1
        print(f"resiver: {frame_count}")
        frame_count = 0
    try:
        try:
            if order[-1] == 1:
                if check_differences(order) == True:
                    photo = b''.join(packs)
                    display.display(photo)
                    #print(order)
                    packs.clear()
                    order.clear()
                    frame_count += 1
                else:
                    packs.clear()
                    order.clear()
        except:
            pass
        data, addr = sock.recvfrom(65500)
        order.append(int(chr(data[-3]))/int(chr(data[-1])))
        data = data[:-3]
        packs.append(data)
    except socket.timeout:
        pass
