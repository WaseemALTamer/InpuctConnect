from pynput.mouse import Listener, Button, Controller

global mouse
mouse = Controller()

global left
global right
left = False
right = False

def Switch_left(state):
    if state == "Lp":
        mouse.press(Button.left)
    else:
        mouse.release(Button.left)
def Switch_right(state):
        if state == "Rp":
            mouse.press(Button.right)
        else:
            mouse.release(Button.right)


def move_mouse(x, y):
    mouse.position = (x, y)

def vector_move(x,y):
    mouse.move(x,y)

def position():
    mouse.position
    return mouse.position

def on_click(x ,y ,button, pressed):
    global left
    global right
    if button == Button.left:
        if pressed:
            left = True
            right = False
        else:
            left = False
            right = False
    elif button == Button.right:
        if pressed:
            right = True
            left = False
        else:
            right = False
            left = False

def start_listener():
    with Listener(on_click=on_click) as listener:
        listener.join()