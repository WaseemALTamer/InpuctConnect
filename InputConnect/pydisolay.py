from screeninfo import get_monitors
import pygame
import time
import io


state = False
data = b""
fps = 0
timer = time.time() + 1

monitor = get_monitors()[0]
display_width = monitor.width
display_height = monitor.height

def display(photo_data):
    global window, timer, fps, display_width, display_height
    if time.time() > timer:
        print(fps)
        fps = 0
        timer = time.time() + 1
    try:
        image_data = io.BytesIO(photo_data)
        image = pygame.image.load(image_data)
        resized_image = pygame.transform.scale(image, (display_width , display_height))
        window.blit(resized_image, (0, 0))
        pygame.display.update()
        fps += 1
    except:
        pass

def run(photo_data):
    global state, window, data, display_width, display_height
    if photo_data != b"" and state == False:
        pygame.init()
        window = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
        state = True
    if photo_data == data:
        pygame.display.update()
    else:
        display(photo_data)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pass
    data = photo_data
    pygame.display.update()

        
    