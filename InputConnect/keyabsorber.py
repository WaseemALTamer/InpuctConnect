from screeninfo import get_monitors
import tkinter as tk

monitor = get_monitors()[0]
screen_width = monitor.width
screen_height = monitor.height

global state
state = False

def disable_button(event,for_mouse):
    global state
    if event.keysym == "space" or event.keysym == "Tab":
        button.configure(state="disabled")
    if event.keysym == "Escape" and for_mouse == True:
        state = False
        window.destroy()

def enable_button(event):
    if event.keysym == "space" or event.keysym == "Tab":
        button.configure(state="normal")

def disable_close():
    pass

def quiter():
    global state
    state = False
    window.destroy()

def main(for_mouse):
    global window, state, button
    state = True
    window = tk.Toplevel()
    window.attributes('-fullscreen', True)
    window.overrideredirect(True)
    window.configure(bg='#1F1F1F')
    window.protocol("WM_DELETE_WINDOW", disable_close)
    if for_mouse == False:
        button = tk.Button(window, text="X", font=15, bg="red", command=quiter)
        button.place(x=screen_width-30, y=10)
    else:
        pass
    window.bind("<KeyPress>", lambda event: disable_button(event,for_mouse))
    window.bind("<KeyRelease>", enable_button)
    window.mainloop()