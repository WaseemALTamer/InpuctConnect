from screeninfo import get_monitors
import keyboard
import Functions
import threading
import time
import socket
import pygame



global sock, timer, position


UDP_IP = ""
UDP_PORT = 1
sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM) 


position = Functions.position()
locker = True
timer = time.time() + 1
monitor = get_monitors()[0]
screen_width = monitor.width
screen_height = monitor.height

listener_thread = threading.Thread(target=Functions.start_listener)
listener_thread.daemon = True
listener_thread.start()

right = Functions.right
left = Functions.left 

def main(mouseLock,shift):
    global position, timer, sock, screen_height, screen_width, locker, right, left
    if keyboard.is_pressed('z') and keyboard.is_pressed('n') and keyboard.is_pressed('enter'):
        if time.time() > timer:
            timer = time.time() + 1
            locker = not locker

    if mouseLock == False or locker == False:
        if position != Functions.position():
            position = Functions.position()
            if shift == 0:
                cor = f"{position[0]},{position[1]}S"
                try:
                    sock.sendto(cor.encode(), (UDP_IP, UDP_PORT))
                except:
                    pass

            if position[0] <= 0 and shift == 1:
                cor = f"{screen_width + position[0]},{position[1]}S"
                try:
                    sock.sendto(cor.encode(), (UDP_IP, UDP_PORT))
                except:
                    pass

            if position[0] >= screen_width and shift == 2:
                cor = f"{position[0] - screen_width},{position[1]}S"
                try:
                    sock.sendto(cor.encode(), (UDP_IP, UDP_PORT))
                except:
                    pass

            if position[1] <= 0 and shift == 3:
                cor = f"{position[0]},{1080 + position[1]}S"
                try:
                    sock.sendto(cor.encode(), (UDP_IP, UDP_PORT))
                except:
                    pass

            if position[1] >= screen_height and shift == 4:
                cor = f"{position[0]},{position[1] - screen_height}S"
                try:
                    sock.sendto(cor.encode(), (UDP_IP, UDP_PORT))
                except:
                    pass
            

    if mouseLock == True and locker == True:
        position = Functions.position()
        cor = f"{position[0]-int(screen_width/2)},{position[1]-int(screen_height/2)}M"
        try:
            sock.sendto(cor.encode(), (UDP_IP, UDP_PORT))
            Functions.move_mouse(screen_width//2,screen_height//2)
        except:
            pass
    if Functions.left != left:
        try:
            if left == True:
                sock.sendto("Lr".encode(), (UDP_IP, UDP_PORT))
            else:
                sock.sendto("Lp".encode(), (UDP_IP, UDP_PORT))     
        except:
            pass
        left = Functions.left
    if Functions.right != right:
        try:
            if right == True:
                sock.sendto("Rr".encode(), (UDP_IP, UDP_PORT))
            else:
                sock.sendto("Rp".encode(), (UDP_IP, UDP_PORT))
        except:
            pass
        right = Functions.right
    pygame.time.wait(3)