from PIL import Image, ImageTk
import tkinter as tk
import Vmonitor
import threading
import subprocess
import webbrowser
import Installation
import os 



global state
state = False
restart_required = False

def quiter():
    global state
    state = False
    window.destroy()


def download():
    Installation.install()
    Installation.extraction()
    Installation.AddBatFiles()
    download_button.config(text="Done",bg="green")

def downTriger():
    download_button.config(text="Installing...",bg="Yellow")
    threading.Thread(target=download).start()


def add_mon():
    try:
        documents_path = os.path.expanduser("~/Documents")
        file_path = f"{documents_path}/InputConnect/usbmmidd_v2/add monitor.bat"
        subprocess.call(file_path, shell=True)
    except:
        download_button.config(text=">Dlownload<",bg="Red")

def add_mon_Triger():
    threading.Thread(target=add_mon).start()

def remove_mon():
    try:
        documents_path = os.path.expanduser("~/Documents")
        file_path = f"{documents_path}/InputConnect/usbmmidd_v2/remove monitor.bat"
        subprocess.call(file_path, shell=True)
    except:
        download_button.config(text=">Dlownload<",bg="Red")

def remove_mon_Triger():
    threading.Thread(target=remove_mon).start()


def setting_open():
    global restart_required
    subprocess.Popen("control desk.cpl")
    restart_required = True


def main():
    global window, state, download_button
    state = True
    window = tk.Toplevel()
    window.resizable(width=False, height=False)
    window.title("DSIAPLAY SETUP")
    window.iconbitmap("images/icone.ico")
    window.geometry("400x600")
    window.configure(bg='#232323')
    img = ImageTk.PhotoImage(Image.open("images/VMo.png").resize((int(400),int(600))))
    background = tk.Label(window, image=img, highlightthickness=0, bd=0)



    titel = tk.Label(window,text="VIRTUAL MONITOR",font=30)
    download_button = tk.Button(window,text="Download Files",width=24,height=0,bg="gray",command=downTriger)
    add_mon_button = tk.Button(window,text="Add monitor",width=24,height=0,bg="gray",command=add_mon_Triger)
    remove_mon_button = tk.Button(window,text="Remove monitor",width=24,height=0,bg="gray",command=remove_mon_Triger)
    setting = tk.Button(window,text="Setting",width=18,height=0,bg="gray",command=setting_open)
    
    background.place(x=0,y=0)
    titel.place(x=120,y=0)
    download_button.place(x=50+20,y=120)
    setting.place(x=70,y=560)
    add_mon_button.place(x=50+20,y=300)
    remove_mon_button.place(x=50+20,y=350)
    
    
    window.mainloop()