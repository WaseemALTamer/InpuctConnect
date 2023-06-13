import numpy as np
import cv2

def display(photo_data):
    try:
        jpg_data = np.frombuffer(photo_data, dtype=np.uint8)
        img = cv2.imdecode(jpg_data, cv2.IMREAD_COLOR)
        cv2.namedWindow('video', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow('video', img)
        cv2.waitKey(1)

    except:
        pass