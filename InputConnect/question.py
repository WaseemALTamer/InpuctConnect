from PIL import Image, ImageTk
import tkinter as tk


global state
state = False


def quiter():
    global state
    state = False
    window.destroy()


def display(number):
    pass

def main(number):
    global window, state, fill
    state = True
    window = tk.Toplevel()
    window.resizable(width=False, height=False)
    window.title("question")
    window.iconbitmap("images/icone.ico")
    window.geometry("800x600")
    window.configure(bg='#232323')

    ##

    ##



    display(number)
    window.mainloop()