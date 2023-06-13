import socket
import image
import time
import pygame

global ip, port, buffer, fps, fimer, uav

ip = "192.168.1.171"
port = 3003
buffer = 65000
fps = 0
timer = time.time() + 1
uav = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
theadblocker = False


def main(preofmence_mode):
    global ip, port, buffer, fps, timer, uav, theadblocker
    try:
        if preofmence_mode == True:
            cap = image.convert(image.screenshot(preofmence_mode))
        else:   
            cap = image.screenshot1(preofmence_mode)
        segments = [cap[i:i+buffer] for i in range(0, len(cap), buffer)]
        segment_labels = [f"{i+1}/{len(segments)}" for i in range(len(segments))]
        #print(segment_labels)
        #print([len(s) for s in segments])
        while not theadblocker:
            theadblocker = True
            for i in range(0, len(segments)):
                segment = segments[i] + segment_labels[i].encode()
                uav.sendto(segment, (ip, port))
                pygame.time.wait(2)
            fps += 1
            #pygame.time.wait(10)
            #uav.sendto("frame".encode(), (ip, port))
            #print("frame")
            #time.sleep(1/60)
            theadblocker = False
            break   
        if time.time() > timer:
            #print([len(s) for s in segments])
            print(f"sender: {fps}")
            timer = time.time() + 1
            fps = 0
    except:
        pass
