import socket
from pynput import keyboard


UDP_IP = socket.gethostname()
UDP_PORT = 2

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1/60)

key_map = {
    'backspace': keyboard.Key.backspace,
    'space': keyboard.Key.space,
    'tab': keyboard.Key.tab,
    'enter': keyboard.Key.enter,
    'esc': keyboard.Key.esc,
    'f1': keyboard.Key.f1,
    'f2': keyboard.Key.f2,
    'f3': keyboard.Key.f3,
    'f4': keyboard.Key.f4,
    'f5': keyboard.Key.f5,
    'f6': keyboard.Key.f6,
    'f7': keyboard.Key.f7,
    'f8': keyboard.Key.f8,
    'f9': keyboard.Key.f9,
    'f10': keyboard.Key.f10,
    'f11': keyboard.Key.f11,
    'ctrl': keyboard.Key.ctrl,
    'alt': keyboard.Key.alt,
    'shift': keyboard.Key.shift,
    'caps lock': keyboard.Key.caps_lock,
    'ctrl l': keyboard.Key.ctrl_l,
    'up':keyboard.Key.up,
    'down':keyboard.Key.down,
    'right':keyboard.Key.right,
    'left':keyboard.Key.left,
    'ctrl r': keyboard.Key.ctrl_r,
    'alt l': keyboard.Key.alt_l,
    'alt r': keyboard.Key.alt_r,
    'shift l': keyboard.Key.shift_l,
    'shift r': keyboard.Key.shift_r,
    'delete': keyboard.Key.delete,
    'home': keyboard.Key.home,
    'end': keyboard.Key.end,
    'page up': keyboard.Key.page_up,
    'page up': keyboard.Key.page_up,
    'insert': keyboard.Key.insert,
    'num lock': keyboard.Key.num_lock,
    'print screen': keyboard.Key.print_screen,
    'scroll lock': keyboard.Key.scroll_lock,
    'pause': keyboard.Key.pause,
    'menu': keyboard.Key.menu,
    'left windows': keyboard.Key.cmd}
    
def on_press(key_name):
    try:
        try:

            keyboard.Controller().press(key_name)
        except:
            keyboard.Controller().press(key_map[key_name])
    except:
        pass
def on_release(key_name):
    try:
        try:

            keyboard.Controller().release(key_name)
        except:
            keyboard.Controller().release(key_map[key_name])
    except:
        pass
def name(key):
    name = key.split()
    return name



def main():
    try:
        global sock
        try:
            sock.bind((UDP_IP, UDP_PORT))
        except:
            pass
        data, addr = sock.recvfrom(2048)
        key_name = data.decode()
        KAS = name(key_name)
        #print(key_name[:-2])
        #print(KAS)
        try:
            if KAS[-1] == "D":
                on_press(key_name[:-2])
            if KAS[-1] == "U":
                on_release(key_name[:-2])
        except OSError as e:
            print("System Error")
            pass
        except KeyboardInterrupt:
            print("Keybourd Interrupted")
            pass
    except:
        pass