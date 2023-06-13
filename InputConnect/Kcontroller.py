import sys
import socket
import keyboard

global UDP_IP, UDP_PORT, sock, lower
UDP_IP = ""
UDP_PORT = 2


sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM) 
lower = True

def gaming(key, lower):
    if len(key) == 1 and lower == True:
        return key.lower()        
    else:
        return key 
def main():
    global UDP_IP, UDP_PORT, sock, lower
    try:
        try:
            if keyboard.is_pressed('k') and keyboard.is_pressed('p') and keyboard.is_pressed('enter'):
                lower = not lower
                print(f"_________________GAMING MODE {lower}_________________")
            keys = keyboard.read_event()
            if keys.event_type == 'down':
                name = gaming(keys.name, lower) + " D"
                sock.sendto(name.encode(), (UDP_IP, UDP_PORT))
                print(name,"down")
            if keys.event_type == 'up':
                name = gaming(keys.name, lower) + " U"
                sock.sendto(name.encode(), (UDP_IP, UDP_PORT))
                print(name,"up")     
        except OSError as e:
            print(f'An error occurred: {e}')
            pass
        except KeyboardInterrupt:
            pass
        except:
            print("Unexpected error:", sys.exc_info()[0])
            pass
    except:
        print("random crash")
