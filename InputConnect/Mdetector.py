import  socket
import Functions

UDP_IP = socket.gethostname()
UDP_PORT = 1

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

global left
global right

left = False
right = False



def main():
    global sock, left, right 
    try:
        sock.bind((UDP_IP, UDP_PORT))
    except:
        pass
    try:
        data, addr = sock.recvfrom(1042)
        command = data.decode()
        if command[0] != "L" and command != "R"[0] and command[-1] == "M":
            command = command[:-1]
            x, y = command.split(",")
            x = int(x)
            y = int(y)
            Functions.vector_move(x,y)
        if command[0] != "L" and command != "R"[0] and command[-1] == "S":
            command = command[:-1]
            x, y = command.split(",")
            x = int(x)
            y = int(y)
            Functions.move_mouse(x,y)
        if command == "Lp":
            Functions.Switch_left("Lp")
            left = True
        if command == "Lr":
            Functions.Switch_left("Lr")
            left = False
        if command == "Rp":
            Functions.Switch_right("Rp")
            right = True
        if command == "Rr":
            Functions.Switch_right("Rr")
            right = False
        pass
    except OSError as e:
        print("System Error")
        pass
    except KeyboardInterrupt:
        print("Keybourd Interrupted")
        pass

