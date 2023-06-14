from screeninfo import get_monitors


monitor = get_monitors()[0]
screen_width = monitor.width
screen_height = monitor.height
print(f"{screen_width} * {screen_height}")