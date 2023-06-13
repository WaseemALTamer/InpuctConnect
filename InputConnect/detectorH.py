import socket
import display
import time
import threading
import statistics
import pygame
import pydisolay

photo = b""
state = False
port = 9009
thread = 1
once = False
timer2 = time.time() + 2


def window():
    global timer, state, photo
    while state:
        #if time.time() > timer:
            #timer = time.time() + 1
            #print(fps)
        try:
            pydisolay.run(photo)
            pygame.time.wait(3)
        except:
            #with open("images/range.jpg", 'rb') as f:
                #pydisolay.run(f.read())
            pygame.time.wait(3)
    pydisolay.state = False

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)
timer = time.time()
fps = 0
checker = []

def main():
    global timer, fps, photo, sock, state, thread, checker, port, once, timer2

    if state == True and once == False:
        server_address = (socket.gethostname(), port)
        sock.bind(server_address)
        for i in range (0, thread):
            threading.Thread(target=window).start()
        once = True
    while state:
        try:
            sock.listen(1)
            print('Waiting for a client connection...')
            client_sock, client_address = sock.accept()
            print('Accepted connection from', client_address)
            while state:
                if time.time() > timer:
                    timer = time.time() + 1
                    #print(fps)
                    fps = 0
                try:
                    data = client_sock.recv(455000)
                    if len(data) != 0:
                        timer2 = time.time() + 2
                        checker.append(data[-1])
                        if len(checker) == 5:
                            checker = checker[1:]
                        if data[-1] == statistics.mode(checker):
                            #pydisolay.run(data)
                            photo = data
                            pass
                        fps += 1
                    if time.time() > timer2 and len(data) == 0:
                        break
                except socket.timeout:
                    pass
        except socket.error as e:
            print('Error occurred:', e)