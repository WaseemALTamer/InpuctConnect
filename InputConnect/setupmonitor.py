from PIL import Image, ImageTk
import tkinter as tk
import Vmonitor
import threading
import subprocess
import webbrowser




global state
state = False
restart_required = False

def quiter():
    global state
    state = False
    window.destroy()


def download():
    global restart_required
    webbrowser.open('https://www.amyuni.com/downloads/usbmmidd_v2.zip')
    restart_required = True

def remove_mon():
    global restart_required
    threading.Thread(target=Vmonitor.add,args=(-1,)).start()
    restart.place(x=5,y=275)
    restart_required = True

def setting_open():
    global restart_required
    subprocess.Popen("control desk.cpl")
    restart_required = True
    restart.place(x=5,y=400)
def link_hover(event):
    link.config(fg="dark blue")

def link_out(event):
    link.config(fg="light blue")

def open_link(event):
    webbrowser.open('https://www.youtube.com/watch?v=ybHKFZjSkVY')
    restart.place(x=5,y=400)




def main():
    global window, state, link, restart
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
    restart = tk.Label(window,text="""Restart you app to detect the changes if you did not do anything then
    ignore this message!""",bg="dark red",fg="black")
    link.bind("<ButtonRelease-1>", open_link)
    link.bind("<Enter>", link_hover)
    link.bind("<Leave>", link_out)
    titel = tk.Label(window,text="VIRTUAL MONITOR",font=30)
    download_button = tk.Button(window,text="Download Files",width=24,height=0,bg="gray",command=download)
    setting = tk.Button(window,text="Setting",width=18,height=0,bg="gray",command=setting_open)
    
    titel.place(x=120,y=0)
    link.place(x=10,y=300)
    download_button.place(x=50,y=120)
    setting.place(x=70,y=560)
    
    
    window.mainloop()