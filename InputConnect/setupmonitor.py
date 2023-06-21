from PIL import Image, ImageTk
import tkinter as tk
import Vmonitor
import threading
import subprocess
import webbrowser




global state
state = False


def quiter():
    global state
    state = False
    window.destroy()


def add_mon():
    threading.Thread(target=Vmonitor.add,args=(1,)).start()

def remove_mon():
    threading.Thread(target=Vmonitor.add,args=(-1,)).start()

def setting_open():
    subprocess.Popen('control desk.cpl')

def link_hover(event):
    link.config(fg="dark blue")
def link_out(event):
    link.config(fg="light blue")
def open_link(event):
    webbrowser.open('https://www.youtube.com/watch?v=ybHKFZjSkVY')

def main():
    global window, state,link
    state = True
    window = tk.Toplevel()
    window.resizable(width=False, height=False)
    window.title("DSIAPLAY SETUP")
    window.iconbitmap("images/icone.ico")
    window.geometry("400x600")
    window.configure(bg='#232323')

    background = ImageTk.PhotoImage(Image.open("images/VMo.png").resize((int(400),int(600))))
    image_background = tk.Label(window, image=background, highlightthickness=0, bd=0)
    image_background.place(x=0,y=0)
    link = tk.Label(window,text="https://www.youtube.com/watch?v=ybHKFZjSkVY",bg="#323232",fg="light blue")
    link.bind("<ButtonRelease-1>", open_link)
    link.bind("<Enter>", link_hover)
    link.bind("<Leave>", link_out)


    titel = tk.Label(window,text="VIRTUAL MONITOR",font=30)
    add_mon_button = tk.Button(window,text="ADD DISPLAY",width=24,height=0,bg="gray",command=add_mon)
    remove_mon_button = tk.Button(window,text="REMOVE DISPLAY",width=24,height=0,bg="gray",command=remove_mon)
    setting = tk.Button(window,text="Setting",width=18,height=0,bg="gray",command=setting_open)
    link.place(x=10,y=550)
    titel.place(x=120,y=0)
    add_mon_button.place(x=50,y=100)
    remove_mon_button.place(x=90,y=150)
    setting.place(x=160,y=200)
    window.mainloop()
