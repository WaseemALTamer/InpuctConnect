from tkinter import *
from pystray import MenuItem as item
import pystray
from PIL import Image, ImageTk

# Create an instance of tkinter frame or window
win = Tk()

win.title("System Tray Application")
# Set the size of the window
win.geometry("700x350")

# Define a function for quitting the window
def quit_window(icon, item):
    icon.stop()
    win.destroy()

# Define a function to show the window again
def show_window(icon, item):
    icon.stop()
    win.overrideredirect(False)  # Restore window decorations
    win.deiconify()

# Hide the window and show it on the system taskbar
def hide_window():
    win.overrideredirect(True)  # Remove window decorations
    win.withdraw()
    image = Image.open("images/icone.ico")
    menu = (item('Quit', quit_window), item('Show', show_window),item('Open', show_window))
    icon = pystray.Icon("name", image, "My System Tray Icon", menu)
    icon.run()

win.protocol('WM_DELETE_WINDOW', hide_window)

win.mainloop()