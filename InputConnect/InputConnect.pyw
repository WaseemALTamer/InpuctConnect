from pystray import MenuItem as item
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import keyabsorber
import Mdetector
import Kcontroller
import Kdetector
import senderH
import detectorH
import Mmouse
import socket
import screeninfo
import threading
import pydisolay
import resiver
import sender
import image
import time
import Mshift
import pystray
import question



root = tk.Tk()
root.title("InputConnect")
root.iconbitmap("images/icone.ico")
root.resizable(width=False, height=False)
root.configure(bg="#1F1F1F")
host = socket.gethostbyname(socket.gethostname())
monitor_count = len(screeninfo.get_monitors())

hover = False
STATE = True

time_hover = time.time() + 1

resiving_FPS = 0
sendeing_FPS = 0
resiving_timer = 0
sending_timer = 0


###Keybourd
Kdetection_state = False
Kcontroller_state = False
###mouse
Mdetection_state = False
Mcontroller_state = False
###display
display_sender_state = False
display_detector_state = False

def quit_window(icon, item):
    icon.stop()
    root.destroy()


def show_window(icon, item):
    icon.stop()
    root.after(0,root.deiconify)

def item_lunch_absorber(icon, item):
    icon.stop()
    root.after(0,root.deiconify)
    #keyabsorber.main(Mcontroller_state)

def hide_window():
    try:
        question.quiter()
    except:
        pass
    try:
        keyabsorber.quiter()
    except:
        pass
    root.withdraw()
    image = Image.open("images/icone.ico")
    menu = (item('Show', show_window),item('Quit', quit_window))
    icon = pystray.Icon("InputConnect", image, "InputConnect", menu)
    icon.run()


def clear_window(window):
    for widget in window.winfo_children():
        widget.place_forget()


def mouse_detection():
    global Mdetection_state,STATE
    mouse_port_entery.config(state='readonly',fg="gray")
    while Mdetection_state and STATE:
        Mdetector.main()
    mouse_port_entery.config(state='normal',fg="black")

def mouse_controller():
    global Mcontroller_state,Kcontroller_state,display_sender_state,STATE, mouse_locker_boolen
    ip1.config(state='readonly',fg="gray")
    ip2.config(state='readonly',fg="gray")
    ip3.config(state='readonly',fg="gray")
    ip4.config(state='readonly',fg="gray")
    mouse_port_entery.config(state='readonly',fg="gray")
    while Mcontroller_state and STATE:
        Mmouse.main(mouse_locker_boolen,Mshift.shift)
    mouse_port_entery.config(state='normal',fg="black")
    if Kcontroller_state == False and Mcontroller_state == False and display_sender_state == False:
        ip1.config(state='normal',fg="black")
        ip2.config(state='normal',fg="black")
        ip3.config(state='normal',fg="black")
        ip4.config(state='normal',fg="black")
        
def keybourd_detection():
    global Kdetection_state,STATE
    keybourd_port_entery.config(state='readonly',fg="gray")
    while STATE and Kdetection_state:
        Kdetector.main()
    keybourd_port_entery.config(state='normal',fg="black")

def keybourd_controller():
    global Mcontroller_state,Kcontroller_state,display_sender_state,STATE
    ip1.config(state='readonly',fg="gray")
    ip2.config(state='readonly',fg="gray")
    ip3.config(state='readonly',fg="gray")
    ip4.config(state='readonly',fg="gray")
    keybourd_port_entery.config(state='readonly',fg="gray")
    while STATE and Kcontroller_state:
        Kcontroller.main()
    keybourd_port_entery.config(state='normal',fg="black")
    if Kcontroller_state == False and Mcontroller_state == False and display_sender_state == False:
        ip1.config(state='normal',fg="black")
        ip2.config(state='normal',fg="black")
        ip3.config(state='normal',fg="black")
        ip4.config(state='normal',fg="black")

def display_resiver():
    global display_detector_state, display_theads_count
    display_port_entery.config(state='readonly',fg="gray")
    detectorH.thread = display_theads_count
    while STATE and display_detector_state:
        detectorH.main()
    display_port_entery.config(state='normal',fg="black")
    detectorH.state = False
    pydisolay.state = False

def display_sender():
    global Mcontroller_state,Kcontroller_state,display_sender_state,STATE,display_preformence_boolen,display_monitor_target
    ip1.config(state='readonly',fg="gray")
    ip2.config(state='readonly',fg="gray")
    ip3.config(state='readonly',fg="gray")
    ip4.config(state='readonly',fg="gray")
    display_FPS_entry.config(state='readonly',fg="gray")
    display_port_entery.config(state='readonly',fg="gray")
    while STATE and display_sender_state:
        senderH.main(FPS_chcker(),display_monitor_target)
    display_port_entery.config(state='normal',fg="black")
    if Kcontroller_state == False and Mcontroller_state == False and display_sender_state == False:
        ip1.config(state='normal',fg="black")
        ip2.config(state='normal',fg="black")
        ip3.config(state='normal',fg="black")
        ip4.config(state='normal',fg="black")
    display_FPS_entry.config(state='normal',fg="black")
    senderH.state = False
    display_sender_state = False
    image.video_runing = False
    try:
        image.stopcam()
    except:
        pass

def lunch_mouse_detector():
    global Mdetection_state, host, page
    Mdetector.UDP_IP = host
    Mdetector.UDP_PORT = port_checker(mouse_port_entery.get(),"mouse_port_checker")
    if Mdetector.UDP_PORT == None or Mdetector.UDP_IP == None:
        Mdetection_state = False
        mouse_detection_button.configure(text="DETECT",bg="gray")
        return None
    Mdetection_state = not Mdetection_state
    threading.Thread(target=mouse_detection).start()
    if page != 100:
        if page > 0:
            page = -5
            array_page.append(page)
            window1()
        if page <= 0:
            window1()
    if Mdetection_state == True:
        mouse_detection_button.configure(text="STOP" ,bg="red")
    else:
        mouse_detection_button.configure(text="DETECT",bg="gray")

def lunch_mouse_controller():
    global Mcontroller_state, page
    Mmouse.UDP_IP = ip_checker()
    Mmouse.UDP_PORT = port_checker(mouse_port_entery.get(),"mouse_port_checker")
    if Mmouse.UDP_PORT == None or Mmouse.UDP_IP == None:
        Mcontroller_state = False
        mouse_controller_button.configure(text="CONTROLL",bg="gray")
        return None
    Mcontroller_state = not Mcontroller_state
    threading.Thread(target=mouse_controller).start()
    if page != 100:
        if page > 0:
            page = -5
            array_page.append(page)
            window1()
        if page <= 0:
            window1()
    if Mcontroller_state == True:
        mouse_controller_button.configure(text="STOP" ,bg="red")
    else:
        mouse_controller_button.configure(text="CONTROLL",bg="gray")

def lunch_keybourd_detector():
    global Kdetection_state, host, page
    Kdetector.UDP_IP = host
    Kdetector.UDP_PORT = port_checker(keybourd_port_entery.get(),"keybourd_port_checker")
    if Kdetector.UDP_IP == None or Kdetector.UDP_PORT == None:
        Kdetection_state = False
        keybourd_detection_button.configure(text="DETECT",bg="gray")
        return None
    Kdetection_state = not Kdetection_state
    threading.Thread(target=keybourd_detection).start()
    if page != 100:
        if page > 0:
            page = -5
            array_page.append(page)
            window1()
        if page <= 0:
            window1()
    if Kdetection_state == True:
        keybourd_detection_button.configure(text="STOP" ,bg="red")
    else:
        keybourd_detection_button.configure(text="DETECT",bg="gray")

def lunch_keybourd_controller():
    global Kcontroller_state, page
    Kcontroller.UDP_IP = ip_checker()
    Kcontroller.UDP_PORT = port_checker(keybourd_port_entery.get(),"keybourd_port_checker")
    if Kcontroller.UDP_IP == None or Kcontroller.UDP_PORT == None:
        Kcontroller_state = False
        keybourd_controller_button.configure(text="CONTROLL",bg="gray")
        return None
    Kcontroller_state = not Kcontroller_state
    threading.Thread(target=keybourd_controller).start()
    if page != 100:
        if page > 0:
            page = -5
            array_page.append(page)
            window1()
        if page <= 0:
            window1()
    if Kcontroller_state == True:
        keybourd_controller_button.configure(text="STOP" ,bg="red")
    else:
        keybourd_controller_button.configure(text="CONTROLL",bg="gray")


def lunch_display_detector():
    global display_detector_state, host, page
    detectorH.port = port_checker(display_port_entery.get(),"display_port_checker")
    if  detectorH.port == None:
        display_detector_state = False
        display_detection_button.configure(text="RECIVER",bg="gray")
        return None
    display_detector_state = not display_detector_state
    detectorH.state = True
    threading.Thread(target=display_resiver).start()
    if page != 100:
        if page > 0:
            page = -5
            array_page.append(page)
            window1()
        if page <= 0:
            window1()
    if display_detector_state == True:
        display_detection_button.configure(text="STOP",bg="red")
    else:
        display_detection_button.configure(text="RECIVER",bg="gray")
        detectorH.state = False

def lunch_display_sender():
    global display_sender_state, display_theads_count, page
    senderH.ip = ip_checker()
    senderH.port = port_checker(display_port_entery.get(),"display_port_checker")
    fps_local = FPS_chcker()
    if fps_local == None:
        display_sender_state = False
        return None
    if senderH.ip == None or senderH.port == None:
        display_sender_state = False
        display_controller_button.configure(text="SENDER",bg="gray")
        return None
    display_sender_state = not display_sender_state
    threading.Thread(target=display_sender).start()
    if page != 100:
        if page > 0:
            page = -5
            array_page.append(page)
            window1()
        if page <= 0:
            window1()
    if display_sender_state == True:
        display_controller_button.configure(text="STOP",bg="red")
    else:
        display_controller_button.configure(text="SENDER",bg="gray")
        senderH.state = False


def keys_absorber_button_set():
    keybourd_absorber_button.configure(text="ABSORBER",bg="gray")

def key_absorber_state_button():
    if keyabsorber.state == True:
        root.after(500,key_absorber_state_button)
    if keyabsorber.state == False:
        keybourd_absorber_button.configure(text="ABSORBER",bg="gray")
        return None

def keys_absorber():
    global Mcontroller_state
    if keyabsorber.state == False:
        keyabsorber.state = True
        keybourd_absorber_button.configure(text="ABSORBER",bg="green")
        root.after(16,key_absorber_state_button)
        keyabsorber.main(Mcontroller_state)
        
    else:
        keybourd_absorber_button.configure(text="ALREADY ON",bg="yellow")
        root.after(16,key_absorber_state_button)

def mouse_shifter():
    if Mshift.state == False:
        Mshift.state = True
        Mshift.main()
    if Mshift.state == True:
        return None
        

def display_thead_increase():
    global display_theads_count
    display_theads_count += 1
    if display_theads_count >= 6:
        display_theads_count_label.configure(fg="yellow")
    if display_theads_count >= 10:
        display_theads_count_label.configure(fg="red")
    display_theads_count_label.configure(text=f"{display_theads_count}")


def display_thead_decrease():
    global display_theads_count
    if display_theads_count == 1:
        return None
    display_theads_count -= 1
    if display_theads_count < 10:
        display_theads_count_label.configure(fg="yellow")
    if display_theads_count < 6:
        display_theads_count_label.configure(fg="green")
    display_theads_count_label.configure(text=f"{display_theads_count}")

def display_monitor_button_forward_fun():
    global monitor_count, display_monitor_target
    if monitor_count - 1 > display_monitor_target:
        display_monitor_target += 1
    display_monitor_target_label.config(text=f"{display_monitor_target}")

def display_monitor_button_backward_fun():
    global monitor_count, display_monitor_target
    if display_monitor_target > 0:
        display_monitor_target -= 1
    display_monitor_target_label.config(text=f"{display_monitor_target}")

def display_box_boolen():
    global display_preformence_boolen, display_sender_state, display_theads_count
    display_preformence_boolen = not display_preformence_boolen
    if display_preformence_boolen == True:
        display_thread_label.place(x=1000,y=430+80)
        display_theads_count_label.place(x=1135,y=425+80)
        display_theads_right.place(x=1170,y=430+80)
        display_theads_left.place(x=1110,y=430+80)
    if display_preformence_boolen == False:
        display_thread_label.place_forget()
        display_theads_count_label.place_forget()
        display_theads_right.place_forget()
        display_theads_left.place_forget()
        display_sender_state = False
        display_controller_button.configure(text="SENDER",bg="gray")
        display_theads_count = 1
        display_theads_count_label.configure(text=f"{display_theads_count}")


def mouse_box_bollen():
    global mouse_locker_boolen
    mouse_locker_boolen = not mouse_locker_boolen

def ip_checker():
    if ip1.get() == "" or ip2.get() == "" or ip3.get() == "" or ip4.get() == "":
        ip_label.config(text="IP: ERROR", bg="dark red")
        return None
    else:
        ip_label.config(text=f"IP:{ip1.get()}.{ip2.get()}.{ip3.get()}.{ip4.get()}",bg="#1F1F1F")
        return f"{ip1.get()}.{ip2.get()}.{ip3.get()}.{ip4.get()}"
    
def FPS_chcker():
    fpslocal = display_FPS_entry.get()
    try:
        fpslocal = int(fpslocal)
        display_FPS_lable.config(bg="#1F1F1F",fg="gray")
        return int(fpslocal)
    except:
        display_FPS_lable.config(text="FPS", bg="dark red")
        return None
    
def port_checker(gateway,name):
    if gateway == "":
        map[name].config(text=f"PORT:_____ XX (0-65535)",bg="dark red")
        return None
    try:
        gateway = int(gateway)
    except:
        map[name].config(text=f"Port: NUMBERS ONLY!",bg="dark red")
        return None
    if gateway > 65535:
        map[name].config(text=f"PORT:{gateway} XX (0-65535)",bg="dark red")
        return None
    map[name].config(text=f"PORT:{gateway}",bg="#1F1F1F")
    if mouse_port_entery.get() == keybourd_port_entery.get() and mouse_port_entery.get() == display_port_entery.get():
        mouse_port_label.config(bg="yellow")
        keybourd_port_label.config(bg="yellow")
        display_port_label.config(bg="yellow")
        return None
    if mouse_port_entery.get() == keybourd_port_entery.get():
        if mouse_port_entery.get() == "":
            pass
        else:    
            mouse_port_label.configure(bg="yellow")
            keybourd_port_label.configure(bg="yellow")
            display_port_label.config(bg="#1F1F1F")
            return None
    if keybourd_port_entery.get() == display_port_entery.get():
        if keybourd_port_entery.get() == "":
            pass
        else:
            display_port_label.configure(bg="yellow")
            keybourd_port_label.configure(bg="yellow")
            mouse_port_label.config(bg="#1F1F1F")
            return None
    if mouse_port_entery.get() == display_port_entery.get():
        if mouse_port_entery.get() == "":
            pass
        else:
            mouse_port_label.configure(bg="yellow")
            display_port_label.configure(bg="yellow")
            keybourd_port_label.config(bg="#1F1F1F")
            return None
    mouse_port_label.config(bg="#1F1F1F")
    keybourd_port_label.config(bg="#1F1F1F")
    display_port_label.config(bg="#1F1F1F")
    save_on_text()
    return gateway



def on_hover_timer(x,y):
    global hover, time_hover, page
    if page == -1:
        if hover == True:
            if time.time() > time_hover:
                if hover == True:
                    if y >= 380:
                        if x >= 900:
                            image_panal4.place(x=x-420,y=y)
                            if x == 960 and y == 380:
                                display_detection_message.place(x=x-400,y=y+20)
                                return None
                            if x == 960 and y == 430:
                                display_sender_message.place(x=x-400,y=y+20)
                                return None
                            if x == 960 and y == 460:
                                display_prefomence_message.place(x=x-400,y=y+20)
                                return None
                            return None
                        else:
                            image_panal3.place(x=x,y=y-120)
                            if x == 260 and y == 500:
                                mouse_detection_message.place(x=x+55,y=y-95)
                                return None
                            if x == 260 and y == 550:
                                mouse_conrtoller_message.place(x=x+55,y=y-95)
                                return None
                            if x == 200 and y == 590:
                                mouse_checkbox_message.place(x=x+55,y=y-95)
                                return None
                            if x == 740 and y == 500:
                                keybourd_detection_message.place(x=x+55,y=y-95)
                                return None
                            if x == 740 and y == 550:
                                keyrboud_conrtoller_message.place(x=x+55,y=y-95)
                                return None
                            if x == 740 and y == 600:
                                keybourd_absorber_message.place(x=x+55,y=y-95)
                                return None
                            return None
                    else:
                        if x >= 900:
                            if x == 980 and y == 350:
                                image_panal4.place(x=560,y=340)
                                display_theads_message.place(x=x-400, y=y + 10)
                                return None
                            if x == 740 and y == 600:
                                image_panal4.place(x=x,y=y)
                                keybourd_absorber_message.place(x=x,y=y-95)
                                return None
                            image_panal2.place_forget()
                            image_panal2.place(x=x-420,y=y)
                            port_message.place(x=x-400,y=y+30)
                            return None
                        else:
                            image_panal.place_forget()
                            image_panal.place(x=x,y=y)
                            if y == 350:
                                port_message.place(x=x+60,y=y+30)
                                return None
                            if y == 90:
                                ip_message.place(x=x+60,y=y+30)
                                return None
                            return None
            root.after(16, lambda: on_hover_timer(x,y))
        else:
            return None

def on_hover(event,x,y):
    global hover, time_hover
    return None
    hover = True
    time_hover = time.time() + 1
    root.after(16, lambda: on_hover_timer(x,y))
        
def out_hover(event):
    return None
    global hover
    image_panal.place_forget()
    image_panal2.place_forget()
    image_panal3.place_forget()
    image_panal4.place_forget()
    port_message.place_forget()
    ip_message.place_forget()
    mouse_checkbox_message.place_forget()
    mouse_detection_message.place_forget()
    mouse_conrtoller_message.place_forget()
    keybourd_absorber_message.place_forget()
    keybourd_detection_message.place_forget()
    keyrboud_conrtoller_message.place_forget()
    display_sender_message.place_forget()
    display_theads_message.place_forget()
    display_detection_message.place_forget()
    display_sender_message.place_forget()
    display_prefomence_message.place_forget()
    hover = False


###### pages
page = -5
array_page = [-5]

def question_window(number):
    if question.state == False:
        question.main(number)
    else:
        question.quiter()
        question.main(number)



def advacned_mode_shift():
    global page, array_page
    try:
        question.quiter()
    except:
        pass
    try:
        keyabsorber.quiter()
    except:
        pass
    if page >= -5 and page != 100:
        page = 100
        window_advance()
    else:
        page = -5
        window1()

def window_page_back(event):
    global page, array_page
    try:
        question.quiter()
    except:
        pass
    try:
        keyabsorber.quiter()
    except:
        pass
    array_page = array_page[:-1]
    page = array_page[-1]
    if Mshift.state == True:
        Mshift.quiter()    
    window1()

def window_page_0():
    global page, array_page
    page = 0
    array_page.append(page)
    window1()

def window_page_start():
    global page, array_page
    page = -5
    array_page.append(page)
    window1()

def window_page_setup_keybourd():
    global page, array_page
    page = -4
    array_page.append(page)
    window1()

def window_page_setup_mouse():
    global page, array_page
    page = -3
    array_page.append(page)
    window1()

def window_page_setup_display():
    global page, array_page
    page = -2
    array_page.append(page)
    window1()

def keybourd_detection_page():
    global page, array_page
    page = 1
    array_page.append(page)
    window1()
    
def keybourd_controller_page():
    global page, array_page
    page = 2
    array_page.append(page)
    window1()

def mouse_detection_page():
    global page, array_page
    page = 3
    array_page.append(page)
    window1()
    
def mouse_controller_page():
    global page, array_page
    page = 4
    array_page.append(page)
    window1()

def display_resiver_page():
    global page, array_page
    page = 5
    array_page.append(page)
    window1()

def display_sender_page():
    global page, array_page
    page = 6
    array_page.append(page)
    window1()


def back_button_fun1(event):
    image_back_button.config(image=back_button)


def back_button_fun2(event):
    image_back_button.config(image=back_button1)

def qusetion__hover_over(argument):
    if argument == 1:
        image_qusetion_ip.config(image=qusetion2)
    if argument == 2:
        image_qusetion_mouse.config(image=qusetion2)
    if argument == 3:
        image_qusetion_keybourd.config(image=qusetion2)
    if argument == 4:
        image_qusetion_display.config(image=qusetion2)
    if argument == 5:
        image_qusetion_mouse_detect_page.config(image=qusetion2)
    if argument == 6:
        image_qusetion_mouse_control_page.config(image=qusetion2)
    if argument == 7:
        image_qusetion_keybourd_detect_page.config(image=qusetion2)
    if argument == 8:
        image_qusetion_keybourd_control_page.config(image=qusetion2)
    if argument == 9:
        image_qusetion_display_recive_page.config(image=qusetion2)
    if argument == 10:
        image_qusetion_display_send_page.config(image=qusetion2)
    if argument == 0:
        image_qusetion_general_page.config(image=qusetion2)


def qusetion__hover_exit(argument):
    if argument == 1:
        image_qusetion_ip.config(image=qusetion)
    if argument == 2:
        image_qusetion_mouse.config(image=qusetion)
    if argument == 3:
        image_qusetion_keybourd.config(image=qusetion)
    if argument == 4:
        image_qusetion_display.config(image=qusetion)
    if argument == 5:
        image_qusetion_mouse_detect_page.config(image=qusetion)
    if argument == 6:
        image_qusetion_mouse_control_page.config(image=qusetion)
    if argument == 7:
        image_qusetion_keybourd_detect_page.config(image=qusetion)
    if argument == 8:
        image_qusetion_keybourd_control_page.config(image=qusetion)
    if argument == 9:
        image_qusetion_display_recive_page.config(image=qusetion)
    if argument == 10:
        image_qusetion_display_send_page.config(image=qusetion)
    if argument == 0:
        image_qusetion_general_page.config(image=qusetion)



def save_on_text():
    temp = []
    temp.append(ip1.get())
    temp.append(ip2.get())
    temp.append(ip3.get())
    temp.append(ip4.get())
    temp.append(mouse_port_entery.get())
    temp.append(keybourd_port_entery.get())
    temp.append(display_port_entery.get())
    try:
        with open("config.txt","w") as file:
            for i in range(0,len(temp)):
                file.write(str(temp[i]) + "\n")
    except:
        pass



def window1():
    global page,Kdetection_state ,Kcontroller_state, Mcontroller_state ,Mdetection_state ,display_detector_state , display_sender_state, monitor_count
    clear_window(root)
    root.geometry("400x600")
    advanced_mode_checkbox.place(x=0,y=570)
    
    
    if page == -5:
        image_background_page5.place(x=0,y=0)
        connect_titel.place(x=60,y=5)
        keybourd_titel.place(x=60,y=60)
        if Kdetection_state == True:
            keybourd_detection_button.place(x=80,y=100)
        elif Kcontroller_state == True:
            keybourd_controller_button.place(x=80,y=100)
            keybourd_absorber_button.place(x=80,y=130)
        else:
            connect_keybourd_button.place(x=80,y=100)

        mouse_titel.place(x=60,y=240)
        if Mdetection_state == True:
            mouse_detection_button.place(x=80,y=270)
        elif Mcontroller_state == True:
            mouse_controller_button.place(x=80,y=270)
            if monitor_count > 1:
                mouse_shift_button.place(x=80,y=320)
                mouse_locker_checkbox.place(x=80,y=295)
            else:
                mouse_locker_checkbox.place(x=80,y=325)
        else:
            connect_mouse_button.place(x=80,y=280)
        display_titel.place(x=60,y=420)
        if display_detector_state == True:
            display_detection_button.place(x=80,y=450)
        elif display_sender_state == True:
            display_controller_button.place(x=80,y=450)
        else:
            connect_display_button.place(x=80,y=460)



    if page == -4:
        image_background_page2.place(x=0,y=0)
        your_ip.place(x=105,y=0)
        keybourd_titel.place(x=40,y=60)
        image_qusetion_general_page.place(x=385,y=5)
        if Kdetection_state == True:
            keybourd_detection_button.place(x=140,y=100+200)
        elif Kcontroller_state == True:
            keybourd_controller_button.place(x=140,y=140+200)
            keybourd_absorber_button.place(x=170,y=170+200)
        else:
            keybourd_page_detection.place(x=50,y=100+150)
            keybourd_page_control.place(x=140,y=140+200)
        image_back_button.place(x=3,y=3)

 
    if page == -3:
        image_background_page2.place(x=0,y=0)
        your_ip.place(x=105,y=0)
        mouse_titel.place(x=40+15,y=60)
        image_qusetion_general_page.place(x=385,y=5)
        if Mdetection_state == True:
            mouse_detection_button.place(x=140,y=270+200)
        elif Mcontroller_state == True:
            mouse_controller_button.place(x=140,y=270+200)
            if monitor_count > 1:
                mouse_shift_button.place(x=140,y=330+200)
                mouse_locker_checkbox.place(x=140,y=300+200)
            else:
                mouse_locker_checkbox.place(x=140,y=330+200)
        else:
            mouse_page_detection.place(x=50,y=100+150)
            mouse_page_control.place(x=140,y=140+200)
        image_back_button.place(x=3,y=3)


    if page == -2:
        image_background_page2.place(x=0,y=0)
        your_ip.place(x=105,y=0)
        display_titel.place(x=40+15,y=60)
        image_qusetion_general_page.place(x=385,y=5)
        if display_detector_state == True:
            display_detection_button.place(x=140,y=450+200)
        elif display_sender_state == True:
            display_controller_button.place(x=140,y=450+200)
        else:
            display_page_resive.place(x=50,y=100+150)
            display_page_sender.place(x=140,y=140+200)
        image_back_button.place(x=3,y=3)
        

    if page == -1:
        pass


    if page == 0:
        connect_processes_lable.place(x=150,y=5)
        keybourd_titel.place(x=40,y=60)
        image_qusetion_general_page.place(x=385,y=5)
        if Kdetection_state == True:
            keybourd_detection_button.place(x=140,y=100)
        elif Kcontroller_state == True:
            keybourd_controller_button.place(x=140,y=140)
            keybourd_absorber_button.place(x=170,y=170)
        else:
            keybourd_page_detection.place(x=50,y=100)
            keybourd_page_control.place(x=140,y=140)
        image_back_button.place(x=3,y=3)

        mouse_titel.place(x=40,y=240)
        if Mdetection_state == True:
            mouse_detection_button.place(x=140,y=270)
        elif Mcontroller_state == True:
            mouse_controller_button.place(x=140,y=270)
            if monitor_count > 1:
                mouse_shift_button.place(x=140,y=330)
                mouse_locker_checkbox.place(x=140,y=300)
            else:
                mouse_locker_checkbox.place(x=140,y=330)
        else:
            mouse_page_detection.place(x=50,y=280)
            mouse_page_control.place(x=140,y=320)

        display_titel.place(x=40,y=420)
        if display_detector_state == True:
            display_detection_button.place(x=140,y=450)
        elif display_sender_state == True:
            display_controller_button.place(x=140,y=450)
        else:
            display_page_resive.place(x=50,y=460)
            display_page_sender.place(x=140,y=500)

    if page == 1:
        image_background_page_general.place(x=0,y=0)
        keybourd_titel.place(x=40,y=60)
        your_ip.place(x=105,y=0)
        keybourd_port_label.place(x=75,y=110)
        keybourd_port_entery.place(x=75,y=140)
        keybourd_detection_button.place(x=75,y=250)
        image_back_button.place(x=3,y=3)
        image_qusetion_keybourd_detect_page.place(x=385,y=5)

    if page == 2:
        image_background_page_general.place(x=0,y=0)
        keybourd_titel.place(x=40,y=60)
        ip_label.place(x=75,y=110)
        ip_postion_enterys = (75,140)
        ip1.place(x=ip_postion_enterys[0]+60*0, y=ip_postion_enterys[1])
        ip2.place(x=ip_postion_enterys[0]+60*1, y=ip_postion_enterys[1])
        ip3.place(x=ip_postion_enterys[0]+60*2, y=ip_postion_enterys[1])
        ip4.place(x=ip_postion_enterys[0]+60*3, y=ip_postion_enterys[1])
        keybourd_port_label.place(x=75,y=210)
        keybourd_port_entery.place(x=75,y=240)
        keybourd_controller_button.place(x=75,y=300)
        image_back_button.place(x=3,y=3)
        image_qusetion_keybourd_control_page.place(x=385,y=5)
        
    if page == 3:
        image_background_page_general.place(x=0,y=0)
        mouse_titel.place(x=40+15,y=60)
        your_ip.place(x=105,y=0)
        mouse_port_label.place(x=75,y=110)
        mouse_port_entery.place(x=75,y=140)
        mouse_detection_button.place(x=75,y=250)
        image_back_button.place(x=3,y=3)
        image_qusetion_mouse_detect_page.place(x=385,y=5)


    if page == 4:
        image_background_page_general.place(x=0,y=0)
        mouse_titel.place(x=40+15,y=60)
        ip_label.place(x=75,y=110)
        ip_postion_enterys = (75,140)
        ip1.place(x=ip_postion_enterys[0]+60*0, y=ip_postion_enterys[1])
        ip2.place(x=ip_postion_enterys[0]+60*1, y=ip_postion_enterys[1])
        ip3.place(x=ip_postion_enterys[0]+60*2, y=ip_postion_enterys[1])
        ip4.place(x=ip_postion_enterys[0]+60*3, y=ip_postion_enterys[1])
        mouse_port_label.place(x=75,y=210)
        mouse_port_entery.place(x=75,y=240)
        mouse_controller_button.place(x=75,y=300)
        image_back_button.place(x=3,y=3)
        image_qusetion_mouse_control_page.place(x=385,y=5)


    if page == 5:
        image_background_page_general.place(x=0,y=0)
        display_titel.place(x=40+15,y=60)
        your_ip.place(x=105,y=0)
        display_port_label.place(x=75,y=110)
        display_port_entery.place(x=75,y=140)
        display_thread_label.place(x=1000-925,y=200)
        display_theads_count_label.place(x=1135-925,y=195)
        display_theads_right.place(x=1170-925,y=200)
        display_theads_left.place(x=1110-925,y=200)
        display_detection_button.place(x=75,y=250)
        image_back_button.place(x=3,y=3) 
        image_qusetion_display_recive_page.place(x=385,y=5)

    if page == 6:
        image_background_dsiplay_sender.place(x=0,y=0)
        display_titel.place(x=40+15,y=60)
        ip_label.place(x=75,y=110)
        ip_postion_enterys = (75,140)
        ip1.place(x=ip_postion_enterys[0]+60*0, y=ip_postion_enterys[1])
        ip2.place(x=ip_postion_enterys[0]+60*1, y=ip_postion_enterys[1])
        ip3.place(x=ip_postion_enterys[0]+60*2, y=ip_postion_enterys[1])
        ip4.place(x=ip_postion_enterys[0]+60*3, y=ip_postion_enterys[1])
        display_port_label.place(x=75,y=210)
        display_port_entery.place(x=75,y=240)
        display_monitor_lable.place(x=1000-925,y=300)
        display_monitor_button_backward.place(x=1110-925,y=300)
        display_monitor_button_forward.place(x=1170-925,y=300)
        display_monitor_target_label.place(x=1135-925,y=295)
        display_FPS_lable.place(x=75,y=350)
        display_FPS_entry.place(x=135,y=350)
        display_controller_button.place(x=75,y=400)
        image_back_button.place(x=3,y=3)
        image_qusetion_display_send_page.place(x=385,y=5)

def window_advance():
    global monitor_count
    clear_window(root)
    root.geometry("1280x720")
    advanced_mode_checkbox.place(x=0,y=690)
    ##general
    image_background.place(x=0,y=0)
    your_ip.place(x=540,y=0)
    ip_label.place(x=520,y=110)
    ip_postion_enterys = (520,140)
    ip1.place(x=ip_postion_enterys[0]+60*0, y=ip_postion_enterys[1])
    ip2.place(x=ip_postion_enterys[0]+60*1, y=ip_postion_enterys[1])
    ip3.place(x=ip_postion_enterys[0]+60*2, y=ip_postion_enterys[1])
    ip4.place(x=ip_postion_enterys[0]+60*3, y=ip_postion_enterys[1])
    #ip_sub.place(x=520,y=170)
    ##mouse
    mouse_titel.place(x=50,y=300)
    mouse_port_label.place(x=50,y=370)
    mouse_port_entery.place(x=50,y=400)
    #mouse_port_sub.place(x=50,y=430)
    mouse_detection_button.place(x=50,y=550)
    mouse_controller_button.place(x=50,y=600)
    mouse_locker_checkbox.place(x=50,y=635)
    mouse_shift_button.place(x=65,y=500)
    #exclamation_image_mouse_port.place(x=250,y=375)
    #exclamation_image_mouse_shift.place(x=230,y=505)
    #exclamation_image_mouse_detect.place(x=260,y=555)
    #exclamation_image_mouse_control.place(x=260,y=605)
    #exclamation_image_mouse_checkbox.place(x=165,y=640)
    ##keybourd
    keybourd_titel.place(x=520,y=300)
    keybourd_port_label.place(x=520,y=370)
    keybourd_port_entery.place(x=520,y=400)
    #keybourd_port_sub.place(x=520,y=430)
    keybourd_detection_button.place(x=520,y=550-10)
    keybourd_controller_button.place(x=520,y=600-10)
    keybourd_absorber_button.place(x=520,y=650-10)
    ##display
    display_titel.place(x=990,y=300)
    display_port_label.place(x=990,y=370)
    display_port_entery.place(x=990,y=400)
    #display_port_sub.place(x=990,y=430)
    display_detection_button.place(x=990,y=550-5)
    display_controller_button.place(x=990,y=630-5)
    display_thread_label.place(x=1000,y=430+80-5)
    display_theads_count_label.place(x=1135,y=425+80-5)
    display_theads_right.place(x=1170,y=430+80-5)
    display_theads_left.place(x=1110,y=430+80-5)
    #display_preformence_checkbox.place(x=990,y=630)
    display_FPS_entry.place(x=1050,y=590-5)
    display_FPS_lable.place(x=990,y=590-5)
    display_monitor_lable.place(x=1000,y=430+35-5)
    display_monitor_button_backward.place(x=1110,y=430+35-5)
    display_monitor_button_forward.place(x=1170,y=430+35-5)
    display_monitor_target_label.place(x=1135,y=425+35-5)
    
    image_qusetion_ip.place(x=735,y=115)
    image_qusetion_mouse.place(x=270,y=300)
    image_qusetion_keybourd.place(x=740,y=300)
    image_qusetion_display.place(x=1210,y=300)

def track_mouse_position(event):
    x = event.x
    y = event.y
    print(f"Mouse position - X: {x}, Y: {y}")
#root.bind("<Motion>", track_mouse_position)



#backgrounds
background = ImageTk.PhotoImage(Image.open("images/background.png").resize((1280,720)))
image_background = tk.Label(root, image=background, highlightthickness=0, bd=0,)

background_page5= ImageTk.PhotoImage(Image.open("images/background page-5.png").resize((int(400),int(600))))
image_background_page5 = tk.Label(root, image=background_page5, highlightthickness=0, bd=0)

background_page2= ImageTk.PhotoImage(Image.open("images/background page2.png").resize((int(400),int(600))))
image_background_page2 = tk.Label(root, image=background_page2, highlightthickness=0, bd=0)


background_dsiplay_sender= ImageTk.PhotoImage(Image.open("images/background_display_sender.png").resize((int(400),int(600))))
image_background_dsiplay_sender = tk.Label(root, image=background_dsiplay_sender, highlightthickness=0, bd=0)


background_page_general= ImageTk.PhotoImage(Image.open("images/background_page_general.png").resize((int(400),int(600))))
image_background_page_general = tk.Label(root, image=background_page_general, highlightthickness=0, bd=0)



##general

your_ip = tk.Label(root,text=f"YOUR IP:{host}",font=18,bg="#E4AD3B",fg="#1F1F1F")
ip_label = tk.Label(root,text = f"IP:CLIENT",font=14,bg="#1F1F1F",fg="gray") 
ip1 = tk.Entry(root, width=4, font=('Arial', 14))
ip1.bind("<Enter>", lambda event: on_hover(event, 760, 90))
ip1.bind("<Leave>", out_hover)
ip2 = tk.Entry(root, width=4, font=('Arial', 14))
ip2.bind("<Enter>", lambda event: on_hover(event, 760, 90))
ip2.bind("<Leave>", out_hover)
ip3 = tk.Entry(root, width=4, font=('Arial', 14))
ip3.bind("<Enter>", lambda event: on_hover(event, 760, 90))
ip3.bind("<Leave>", out_hover)
ip4 = tk.Entry(root, width=4, font=('Arial', 14))
ip4.bind("<Enter>", lambda event: on_hover(event, 760, 90))
ip4.bind("<Leave>", out_hover)
ip_sub = tk.Button(root,text="SUBMIT",width=20,height=0,bg="gray",command=ip_checker)
fps_counter_in = tk.Label(root,text=f"FPS:{resiving_FPS}",font=14,bg="#1F1F1F",fg="gray")
fps_counter_out = tk.Label(root,text=f"FPS:{sendeing_FPS}",font=14,bg="#1F1F1F",fg="gray")
###mouse
mouse_titel = tk.Label(root,text="MOUSE",font=14,bg="#1F1F1F",fg="gray")
mouse_port_label = tk.Label(root,text="PORT:",font=14,bg="#1F1F1F",fg="gray")
mouse_port_entery = tk.Entry(root,width=17,font=("Arial", 14))
mouse_port_entery.bind("<Enter>", lambda event: on_hover(event, 290, 350))
mouse_port_entery.bind("<Leave>", out_hover)
mouse_port_sub = tk.Button(root,text="SUBMIT",width=20,height=0,bg="gray",command=lambda: port_checker(mouse_port_entery.get(),"mouse_port_checker"))
mouse_detection_button = tk.Button(root,text="DETECT",width=24,height=0,bg="gray",command=lunch_mouse_detector)
mouse_detection_button.bind("<Enter>", lambda event: on_hover(event, 260, 500))
mouse_detection_button.bind("<Leave>", out_hover)
mouse_controller_button = tk.Button(root,text="CONTROL",width=24,height=0,bg="gray",command=lunch_mouse_controller)
mouse_controller_button.bind("<Enter>", lambda event: on_hover(event, 260, 550))
mouse_controller_button.bind("<Leave>", out_hover)
mouse_locker_checkbox = tk.Checkbutton(root,text="MOUSE LOCKER",bg="#1F1F1F",fg="gray",selectcolor="#1F1F1F",activeforeground="gray",command=mouse_box_bollen)
mouse_locker_checkbox.bind("<Enter>", lambda event: on_hover(event, 200, 590))
mouse_locker_checkbox.bind("<Leave>", out_hover)
mouse_locker_boolen = False
mouse_shift_button = tk.Button(root,text="SHIFT",width=20,height=0,bg="gray",command=mouse_shifter)

mouse_page_detection = tk.Button(root,text="RECEIVE",width=18,height=0,bg="gray",command=mouse_detection_page)
mouse_page_control = tk.Button(root,text="SEND",width=18,height=0,bg="gray",command=mouse_controller_page)

##keybourd
keybourd_titel = tk.Label(root,text="KEYBOARD",font=14,bg="#1F1F1F",fg="gray")
keybourd_port_label = tk.Label(root,text="PORT:",font=14,bg="#1F1F1F",fg="gray")
keybourd_port_entery = tk.Entry(root,width=17,font=("Arial", 14))
keybourd_port_entery.bind("<Enter>", lambda event: on_hover(event, 760, 350))
keybourd_port_entery.bind("<Leave>", out_hover)
keybourd_port_sub = tk.Button(root,text="SUBMIT",width=20,height=0,bg="gray",command=lambda: port_checker(keybourd_port_entery.get(),"keybourd_port_checker"))
keybourd_detection_button = tk.Button(root,text="DETECT",width=24,height=0,bg="gray",command=lunch_keybourd_detector)
keybourd_detection_button.bind("<Enter>", lambda event: on_hover(event, 740, 500))
keybourd_detection_button.bind("<Leave>", out_hover)
keybourd_controller_button = tk.Button(root,text="CONTROL",width=24,height=0,bg="gray",command=lunch_keybourd_controller)
keybourd_controller_button.bind("<Enter>", lambda event: on_hover(event, 740, 550))
keybourd_controller_button.bind("<Leave>", out_hover)
keybourd_absorber_button = tk.Button(root,text="ABSORBER",width=24,height=0,bg="gray",command=keys_absorber)
keybourd_absorber_button.bind("<Enter>", lambda event: on_hover(event, 740, 600))
keybourd_absorber_button.bind("<Leave>", out_hover)
keybourd_page_detection = tk.Button(root,text="RECEIVE",width=18,height=0,bg="gray",command=keybourd_detection_page)
keybourd_page_control = tk.Button(root,text="SEND",width=18,height=0,bg="gray",command=keybourd_controller_page)


##display
display_titel = tk.Label(root,text="DISPLAY",font=14,bg="#1F1F1F",fg="gray")
display_port_label = tk.Label(root,text="PORT:",font=14,bg="#1F1F1F",fg="gray")
display_port_entery = tk.Entry(root,width=17,font=("Arial", 14))
display_port_entery.bind("<Enter>", lambda event: on_hover(event, 960, 350))
display_port_entery.bind("<Leave>", out_hover)
display_port_sub = tk.Button(root,text="SUBMIT",width=20,height=0,bg="gray",command=lambda: port_checker(display_port_entery.get(),"display_port_checker"))
display_detection_button = tk.Button(root,text="DETECT",width=24,height=0,bg="gray",command=lunch_display_detector)
display_detection_button.bind("<Enter>", lambda event: on_hover(event, 960, 380))
display_detection_button.bind("<Leave>", out_hover)
display_controller_button = tk.Button(root,text="SEND",width=24,height=0,bg="gray",command=lunch_display_sender)
display_controller_button.bind("<Enter>", lambda event: on_hover(event, 960, 430))
display_controller_button.bind("<Leave>", out_hover)
display_thread_label = tk.Label(root,text="THREADS",font=14,bg="#1F1F1F",fg="purple3")
display_theads_count = 1
display_theads_left = tk.Button(root,text="<",command=display_thead_decrease,bg="gray")
display_theads_right = tk.Button(root,text=">",command=display_thead_increase,bg="gray")
display_theads_count_label = tk.Label(root,text=f"{display_theads_count}",font=("Arial", 18),bg="#1F1F1F",fg="green")
display_thread_label.bind("<Enter>", lambda event: on_hover(event, 980, 350))
display_thread_label.bind("<Leave>", out_hover)
display_theads_left.bind("<Enter>", lambda event: on_hover(event, 980, 350))
display_theads_left.bind("<Leave>", out_hover)
display_theads_right.bind("<Enter>", lambda event: on_hover(event, 980, 350))
display_theads_right.bind("<Leave>", out_hover)
display_preformence_boolen = False
display_preformence_checkbox = tk.Checkbutton(root,text="PERFORMANCE",bg="#1F1F1F",fg="gray",selectcolor="#1F1F1F",activeforeground="gray",command=display_box_boolen)
display_preformence_checkbox.bind("<Enter>", lambda event: on_hover(event, 960, 460))
display_preformence_checkbox.bind("<Leave>", out_hover)
display_FPS_entry = tk.Entry(root, width=4, font=('Arial', 14))
display_FPS_entry.insert(tk.END, "70")
display_FPS_lable = tk.Label(root,text="FPS:",font=14,bg="#1F1F1F",fg="gray")
display_FPS_lable.bind("<Enter>", lambda event: on_hover(event, 960, 430))
display_FPS_lable.bind("<Leave>", out_hover)
display_FPS_entry.bind("<Enter>", lambda event: on_hover(event, 960, 430))
display_FPS_entry.bind("<Leave>", out_hover)
display_monitor_lable = tk.Label(root,text="MONITOR",font=14,bg="#1F1F1F",fg="gray")
display_monitor_button_forward = tk.Button(root,text=">",command=display_monitor_button_forward_fun,bg="gray")
display_monitor_button_backward = tk.Button(root,text="<",command=display_monitor_button_backward_fun,bg="gray")
display_monitor_target = 0
display_monitor_target_label = tk.Label(root,text=f"{display_monitor_target}",font=("Arial", 18),bg="#1F1F1F",fg="gray")
display_page_resive = tk.Button(root,text="RECEIVE",width=18,height=0,bg="gray",command=display_resiver_page)
display_page_sender = tk.Button(root,text="SEND",width=18,height=0,bg="gray",command=display_sender_page)


##hovering
pannal = ImageTk.PhotoImage(Image.open("images/pannal.png").resize((int(1283/3),int(722/3))))
pannal2 = ImageTk.PhotoImage(Image.open("images/pannal2.png").resize((int(1283/3),int(722/3))))
pannal3 = ImageTk.PhotoImage(Image.open("images/pannal3.png").resize((int(1283/3),int(722/3))))
pannal4 = ImageTk.PhotoImage(Image.open("images/pannal4.png").resize((int(1283/3),int(722/3))))
exclamation = ImageTk.PhotoImage(Image.open("images/exclamation.png").resize((int(15),int(15))))
back_button = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((int(30),int(30))))
back_button1 = ImageTk.PhotoImage(Image.open("images/backbutton2.png").resize((int(30),int(30))))
qusetion = ImageTk.PhotoImage(Image.open("images/qusetion.png").resize((int(10),int(15))))
qusetion2 = ImageTk.PhotoImage(Image.open("images/qusetion2.png").resize((int(10),int(15))))






image_panal = tk.Label(root, image=pannal, highlightthickness=0, bd=0)
image_panal2 = tk.Label(root, image=pannal2, highlightthickness=0, bd=0)
image_panal3 = tk.Label(root, image=pannal3, highlightthickness=0, bd=0)
image_panal4 = tk.Label(root, image=pannal4, highlightthickness=0, bd=0,)

image_qusetion_ip = tk.Label(root, image=qusetion, highlightthickness=0, bd=0,)
image_qusetion_ip.bind("<Enter>",lambda event: qusetion__hover_over(1))
image_qusetion_ip.bind("<Leave>",lambda event: qusetion__hover_exit(1))
image_qusetion_ip.bind("<ButtonRelease-1>",lambda event: question_window(1))

image_qusetion_mouse = tk.Label(root, image=qusetion, highlightthickness=0, bd=0,)
image_qusetion_mouse.bind("<Enter>",lambda event: qusetion__hover_over(2))
image_qusetion_mouse.bind("<Leave>",lambda event: qusetion__hover_exit(2))
image_qusetion_mouse.bind("<ButtonRelease-1>", lambda event: question_window(2))

image_qusetion_keybourd = tk.Label(root, image=qusetion, highlightthickness=0, bd=0,)
image_qusetion_keybourd.bind("<Enter>",lambda event: qusetion__hover_over(3))
image_qusetion_keybourd.bind("<Leave>",lambda event: qusetion__hover_exit(3))
image_qusetion_keybourd.bind("<ButtonRelease-1>", lambda event: question_window(3))

image_qusetion_display = tk.Label(root, image=qusetion, highlightthickness=0, bd=0,)
image_qusetion_display.bind("<Enter>",lambda event: qusetion__hover_over(4))
image_qusetion_display.bind("<Leave>",lambda event: qusetion__hover_exit(4))
image_qusetion_display.bind("<ButtonRelease-1>", lambda event: question_window(4))


image_qusetion_mouse_detect_page = tk.Label(root, image=qusetion, highlightthickness=0, bd=0,)
image_qusetion_mouse_detect_page.bind("<Enter>",lambda event: qusetion__hover_over(5))
image_qusetion_mouse_detect_page.bind("<Leave>",lambda event: qusetion__hover_exit(5))
image_qusetion_mouse_detect_page.bind("<ButtonRelease-1>", lambda event: question_window(5))

image_qusetion_mouse_control_page = tk.Label(root, image=qusetion, highlightthickness=0, bd=0,)
image_qusetion_mouse_control_page.bind("<Enter>",lambda event: qusetion__hover_over(6))
image_qusetion_mouse_control_page.bind("<Leave>",lambda event: qusetion__hover_exit(6))
image_qusetion_mouse_control_page.bind("<ButtonRelease-1>", lambda event: question_window(6))


image_qusetion_keybourd_detect_page = tk.Label(root, image=qusetion, highlightthickness=0, bd=0,)
image_qusetion_keybourd_detect_page.bind("<Enter>",lambda event: qusetion__hover_over(7))
image_qusetion_keybourd_detect_page.bind("<Leave>",lambda event: qusetion__hover_exit(7))
image_qusetion_keybourd_detect_page.bind("<ButtonRelease-1>", lambda event: question_window(7))

image_qusetion_keybourd_control_page = tk.Label(root, image=qusetion, highlightthickness=0, bd=0,)
image_qusetion_keybourd_control_page.bind("<Enter>",lambda event: qusetion__hover_over(8))
image_qusetion_keybourd_control_page.bind("<Leave>",lambda event: qusetion__hover_exit(8))
image_qusetion_keybourd_control_page.bind("<ButtonRelease-1>", lambda event: question_window(8))


image_qusetion_display_recive_page = tk.Label(root, image=qusetion, highlightthickness=0, bd=0,)
image_qusetion_display_recive_page.bind("<Enter>",lambda event: qusetion__hover_over(9))
image_qusetion_display_recive_page.bind("<Leave>",lambda event: qusetion__hover_exit(9))
image_qusetion_display_recive_page.bind("<ButtonRelease-1>", lambda event: question_window(9))

image_qusetion_display_send_page = tk.Label(root, image=qusetion, highlightthickness=0, bd=0,)
image_qusetion_display_send_page.bind("<Enter>",lambda event: qusetion__hover_over(10))
image_qusetion_display_send_page.bind("<Leave>",lambda event: qusetion__hover_exit(10))
image_qusetion_display_send_page.bind("<ButtonRelease-1>", lambda event: question_window(10))


image_qusetion_general_page = tk.Label(root, image=qusetion, highlightthickness=0, bd=0,)
image_qusetion_general_page.bind("<Enter>",lambda event: qusetion__hover_over(0))
image_qusetion_general_page.bind("<Leave>",lambda event: qusetion__hover_exit(0))
image_qusetion_general_page.bind("<ButtonRelease-1>", lambda event: question_window(11))


#exclamation_image_mouse_port = tk.Label(root, image=exclamation, highlightthickness=0, bd=0,)
#exclamation_image_mouse_shift = tk.Label(root, image=exclamation, highlightthickness=0, bd=0,)
#exclamation_image_mouse_detect = tk.Label(root, image=exclamation, highlightthickness=0, bd=0,)
#exclamation_image_mouse_control = tk.Label(root, image=exclamation, highlightthickness=0, bd=0,)
#exclamation_image_mouse_checkbox = tk.Label(root, image=exclamation, highlightthickness=0, bd=0,)

####general_window1
image_back_button = tk.Label(root, image=back_button1, bd=0,highlightthickness=0)
image_back_button.bind("<ButtonRelease-1>", window_page_back)
image_back_button.bind("<Enter>", back_button_fun1)
image_back_button.bind("<Leave>", back_button_fun2)
advanced_mode_checkbox = tk.Checkbutton(root,text="ADVANCED MODE",bg="#1F1F1F",fg="gray",selectcolor="#1F1F1F",activeforeground="gray",command=advacned_mode_shift)

connect_titel = tk.Label(root,text="CONNECT AND CONTROL",font=18,bg="#1F1F1F",fg="gray")
connect_processes_lable = tk.Label(root,text="PROCESSES",font=18,bg="#1F1F1F",fg="gray")
connect_processes_button = tk.Button(root,text="PROCESSES",width=18,height=0,bg="yellow",command=window_page_0)
connect_keybourd_button = tk.Button(root,text="SETUP",width=18,height=0,bg="gray",command=window_page_setup_keybourd)
connect_mouse_button = tk.Button(root,text="SETUP",width=18,height=0,bg="gray",command=window_page_setup_mouse)
connect_display_button = tk.Button(root,text="SETUP",width=18,height=0,bg="gray",command=window_page_setup_display)


####storing



try:
    with open("config.txt", "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
    ip1.insert(tk.END, str(lines[0]))
    ip2.insert(tk.END, str(lines[1]))
    ip3.insert(tk.END, str(lines[2]))
    ip4.insert(tk.END, str(lines[3]))
    mouse_port_entery.insert(tk.END, str(lines[4]))
    keybourd_port_entery.insert(tk.END, str(lines[5]))
    display_port_entery.insert(tk.END, str(lines[6]))
except:
    pass


#mapping
map = {"mouse_port_checker" : mouse_port_label,
     "keybourd_port_checker": keybourd_port_label,
     "display_port_checker" : display_port_label,
}

#messages
port_message = tk.Label(text="""Ports are identified by numerical values ranging from 0 to 65535. 
This is where the incoming signles will arrive if this is the resiver
part it only needs the port and not the ip.
""",bg="#323232",fg="yellow",anchor='e', justify='left')
ip_message = tk.Label(text="""IP of the client please write the device of the host in the boxes
provided this will let you send messages to the client through it 
you can use the services thatare provided under underneath if that 
is not the case then that means you dont have access to
the internet""",bg="#323232",fg="yellow",anchor='e', justify='left')
mouse_detection_message = tk.Label(text="""This will detect the mouse signles that are being send by the other
device only the portal is required for this""",bg="#323232",fg="yellow",anchor='e', justify='left')
mouse_conrtoller_message = tk.Label(text="""This will controll the mouse from ther other device portal and ip is 
rquired for this.""",bg="#323232",fg="yellow",anchor='e', justify='left')
mouse_checkbox_message = tk.Label(text="""This will allow you to lock the mouse in the middle of the
screen this also will make the mouse move through vectors rather
than the location of the screen this can be helpfull if you have
more than one monitor if your mouse you can press z-n-enter to
realse the lock on the mouse.""",bg="#323232",fg="yellow",anchor='e', justify='left')
keybourd_detection_message = tk.Label(text="""This detect the keybourd signles that are being sent by the otehr
device just the portl is reqired.""",bg="#323232",fg="yellow",anchor='e', justify='left')
keyrboud_conrtoller_message = tk.Label(text="""This will send the keys that are being pressed note that thi will not
be removeing any of the functionality of the keys your press so
make sure you use the absorber and transfere to a new windows
window through win-tab this requres the portal and the ip.""",bg="#323232",fg="yellow",anchor='e', justify='left')
keybourd_absorber_message = tk.Label(text="""This will absorbe this keys that are being pressed in order to let
you do what ever you want on the other device without worrying
what is happining on the controller side we also recommend to
run the absorber for the mouse if the mouse locker is not on.""",bg="#323232",fg="yellow",anchor='e', justify='left')
display_detection_message = tk.Label(text="""This will detect the images that are being sent only requres the
port.""",bg="#323232",fg="yellow",anchor='e', justify='left')
display_sender_message = tk.Label(text="""This will send the images from this device to the other device
that is connected to the same port, the port and ip are required.""",bg="#323232",fg="yellow",anchor='e', justify='left')
display_prefomence_message = tk.Label(text="""This will limmit the ammount of packets that are being send
through going from your screen size image to 720p this will also
allow you to controll how many theads to use in order to controll
how much prefomence is being used.""",bg="#323232",fg="yellow",anchor='e', justify='left')
display_theads_message = tk.Label(text="""theads that are used to detect the image and display the image
on the screen the more the theads these is the less the latency
and the higher the FPS.""",bg="#323232",fg="yellow",anchor='e', justify='left')





window1()


root.protocol('WM_DELETE_WINDOW', hide_window)

root.mainloop()

STATE = False
detectorH.state = False
senderH.state = False
Kdetection_state = False
Kcontroller_state = False
Mcontroller_state = False
Mdetection_state = False
display_sender_state = False
display_detector_state = False