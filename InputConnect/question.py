from PIL import Image, ImageTk
import tkinter as tk


global state
state = False


def quiter():
    global state
    state = False
    window.destroy()

def main(number):
    global window, state
    state = True
    window = tk.Toplevel()
    window.resizable(width=False, height=False)
    window.title("question")
    window.iconbitmap("images/icone.ico")
    window.geometry("800x600")
    window.configure(bg='#232323')

    ##
    question_1 = ImageTk.PhotoImage(Image.open("images/question_1.png").resize((int(800),int(600))))
    question_2 = ImageTk.PhotoImage(Image.open("images/question_2.png").resize((int(800),int(600))))
    question_3 = ImageTk.PhotoImage(Image.open("images/question_3.png").resize((int(800),int(600))))
    question_4 = ImageTk.PhotoImage(Image.open("images/question_4.png").resize((int(800),int(600))))
    question_5 = ImageTk.PhotoImage(Image.open("images/question_5.png").resize((int(800),int(600))))
    question_6 = ImageTk.PhotoImage(Image.open("images/question_6.png").resize((int(800),int(600))))
    question_7 = ImageTk.PhotoImage(Image.open("images/question_7.png").resize((int(800),int(600))))
    question_8 = ImageTk.PhotoImage(Image.open("images/question_8.png").resize((int(800),int(600))))
    question_9 = ImageTk.PhotoImage(Image.open("images/question_9.png").resize((int(800),int(600))))
    question_10 = ImageTk.PhotoImage(Image.open("images/question_10.png").resize((int(800),int(600))))
    question_11 = ImageTk.PhotoImage(Image.open("images/question_11.png").resize((int(800),int(600))))
    image_question_1 = tk.Label(window, image=question_1, highlightthickness=0, bd=0)
    image_question_2 = tk.Label(window, image=question_2, highlightthickness=0, bd=0)
    image_question_3 = tk.Label(window, image=question_3, highlightthickness=0, bd=0)
    image_question_4 = tk.Label(window, image=question_4, highlightthickness=0, bd=0,)
    image_question_5 = tk.Label(window, image=question_5, highlightthickness=0, bd=0,)
    image_question_6 = tk.Label(window, image=question_6, highlightthickness=0, bd=0,)
    image_question_7 = tk.Label(window, image=question_7, highlightthickness=0, bd=0,)
    image_question_8 = tk.Label(window, image=question_8, highlightthickness=0, bd=0,)
    image_question_9 = tk.Label(window, image=question_9, highlightthickness=0, bd=0,)
    image_question_10 = tk.Label(window, image=question_10, highlightthickness=0, bd=0,)
    image_question_11 = tk.Label(window, image=question_11, highlightthickness=0, bd=0,)
    ##
    if number == 11:
        image_question_1.place(x=0,y=0)
    if number == 5:
        image_question_4.place(x=0,y=0)
    if number == 6:
        image_question_5.place(x=0,y=0)
    if number == 7:
        image_question_2.place(x=0,y=0)
    if number == 8:
        image_question_3.place(x=0,y=0)
    if number == 9:
        image_question_6.place(x=0,y=0)
    if number == 10:
        image_question_7.place(x=0,y=0)
    if number == 1:
        image_question_11.place(x=0,y=0)
    if number == 2:
        image_question_8.place(x=0,y=0)
    if number == 3:
        image_question_9.place(x=0,y=0)
    if number == 4:
        image_question_10.place(x=0,y=0)
    window.mainloop()