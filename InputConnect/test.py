import pystray
from pystray import MenuItem as item

# Define a function to be called when the tray icon is clicked
def on_tray_click(icon, item):
    print("Tray clicked!")

# Create a menu with a single item representing your application
menu = (item('Open', on_tray_click),)

# Create the tray icon with the menu
icon = pystray.Icon("images/icone.ico", menu)

# Run the tray icon
icon.run()