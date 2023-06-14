import socket
import image
import sys
import time
import pygame


ip = ""
port = 9009
state = False

fps = 0
timer = time.time() + 1

#image.run()

def main(FPS,display):
    global fps, timer, ip, port, state
    server_address = (ip, port)
    try:
        if state == False:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(server_address)
            print('Connected to the server')
            state = True
        while state:
            if time.time() > timer:
                print(fps)
                fps = 0
                timer = time.time() + 1
            try:
                message = image.screenshot1(FPS,display)
                #message = image.convert(image.get()[0])
                sock.sendall(message)
                fps += 1
                pygame.time.wait(3)
                #pygame.time.wait(5)
            except OSError as e:
                print(f'An error occurred: {e}')
                break
            except KeyboardInterrupt:
                break
            except:
                print('Unexpected error:', sys.exc_info()[0])
                break      
    except ConnectionRefusedError:
        print('Connection refused. Retrying in 2 seconds...')
        time.sleep(2)
        pass

    except Exception as e:
        print(f'An error occurred: {e}')
        return None