from screeninfo import get_monitors
from PIL import Image, ImageTk
import tkinter as tk


global state
state = False

shift = 0

temp_x = 0
temp_y = 0

def on_close():
    global state
    state = False
    quiter()

def right():
    global shift
    shift = 2

def left():
    global shift
    shift = 1

def above():
    global shift
    shift = 3

def behind():
    global shift
    shift = 4

def defult():
    global shift
    shift = 0


def on_label_click(event):
    global temp_x, temp_y, shift
    if temp_x == 225 and temp_y == 45:
        above()
    if temp_x == 70 and temp_y == 150 :
        left()
    if temp_x == 225 and temp_y == 150 :
        defult()
    if temp_x == 380 and temp_y == 150 :
        right()
    if temp_x == 225 and temp_y == 255 :
        behind()
    quiter()


def on_hover(event,x,y):
    global temp_x, temp_y
    temp_y = int(y)
    temp_x = int(x)
    fill.place(x=x+6,y=y+6)

def out_hover(event):
    fill.place_forget()
    pass

def quiter():
    global state
    state = False
    window.destroy()

def main():
    global window, state, fill
    state = True
    window = tk.Toplevel()
    window.resizable(width=False, height=False)
    window.title("shift")
    window.iconbitmap("images/icone.ico")
    window.geometry("600x400")
    window.configure(bg='#232323')
    img = ImageTk.PhotoImage(Image.open("images/screen.png").resize((int(150),int(100))))
    screen0 = tk.Label(window, image=img, highlightthickness=0, bd=0)
    screen1 = tk.Label(window, image=img, highlightthickness=0, bd=0)
    screen2 = tk.Label(window, image=img, highlightthickness=0, bd=0)
    screen3 = tk.Label(window, image=img, highlightthickness=0, bd=0)
    screen4 = tk.Label(window, image=img, highlightthickness=0, bd=0)
    
    img_fill = ImageTk.PhotoImage(Image.open("images/fill.png").resize((int(138),int(87))))
    fill = tk.Label(window, image=img_fill, highlightthickness=0, bd=0)

    screen0.bind("<Enter>", lambda event: on_hover(event, ((600-150)/2), ((400-100)/2)))
    screen0.bind("<Leave>", out_hover)

    screen1.bind("<Enter>", lambda event: on_hover(event, ((600-150)/2)-155, ((400-100)/2)))
    screen1.bind("<Leave>", out_hover)

    screen2.bind("<Enter>", lambda event: on_hover(event, ((600-150)/2)+155, ((400-100)/2)))
    screen2.bind("<Leave>", out_hover)

    screen3.bind("<Enter>", lambda event: on_hover(event, ((600-150)/2), ((400-100)/2)-105))
    screen3.bind("<Leave>", out_hover)

    screen4.bind("<Enter>", lambda event: on_hover(event, ((600-150)/2), ((400-100)/2)+105))
    screen4.bind("<Leave>", out_hover)
    
    fill.bind("<Enter>", lambda event: on_hover(event, temp_x, temp_y))
    fill.bind("<Leave>", out_hover)
    fill.bind("<Button-1>", on_label_click)


    screen0.place(x=((600-150)/2),y=((400-100)/2))
    screen1.place(x=((600-150)/2)-155,y=((400-100)/2))
    screen2.place(x=((600-150)/2)+155,y=((400-100)/2))
    screen3.place(x=((600-150)/2),y=((400-100)/2)-105)
    screen4.place(x=((600-150)/2),y=((400-100)/2)+105)

    window.protocol("WM_DELETE_WINDOW", on_close)

    window.mainloop()
