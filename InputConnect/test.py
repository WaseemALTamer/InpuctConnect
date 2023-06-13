import detectorH
import senderH
import threading

def fun1():
    detectorH.port = 9009
    detectorH.main()

def fun2():
    senderH.port = 9009
    senderH.ip = "192.168.1.173"
    senderH.main()

threading.Thread(target=fun2).start()