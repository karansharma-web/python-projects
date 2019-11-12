import tkinter
import cv2
from functools import partial
import threading
import PIL.Image, PIL.ImageTk  

import imutils
import time

stream = cv2.VideoCapture("C:\\Users\\karan\\PycharmProjects\\untitled4\\decision review system\\images\\clip.mp4")

flag = 'True'
def play(speed):
    global flag
    #Play video in reverse and forward
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        canvas.create_text(500, 20, fill='red', font='times 25 ',
                           text='End of stream')
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    
    if flag:
        canvas.create_text(150,20,fill= 'red', font ='times 25 ',
        text = 'Decision Pending')
    flag = not flag


def pending(decision):
    #Display decision pending image
    frame = cv2.cvtColor(cv2.imread("C:\\Users\\karan\\PycharmProjects\\untitled4\\decision review system\\images\\pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    #Wait for 2 seconds

    time.sleep(2)

    #Display sponsor image

    frame = cv2.cvtColor(cv2.imread("C:\\Users\\karan\\PycharmProjects\\untitled4\\decision review system\\images\\sponsor.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    #Wait for 2 seconds

    time.sleep(2)

    #Display out or not out image

    if decision == 'out':
        decisionImg = 'C:\\Users\\karan\\PycharmProjects\\untitled4\\decision review system\\images\\out.png'

    else:
        decisionImg = 'C:\\Users\\karan\\PycharmProjects\\untitled4\\decision review system\\images\\not_out.png'

    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)



def out():
    thread = threading.Thread(target=pending ,args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")


def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")



#Dimensions of our main screen
SET_WIDTH = 637
SET_HEIGHT = 359

#Tkinter gui starts here

window = tkinter.Tk()
window.title("Next gen decision review system")
cv_img = cv2.cvtColor(cv2.imread("C:\\Users\\karan\\PycharmProjects\\untitled4\\decision review system\\images\\welcome.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0,anchor=tkinter.NW, image=photo)
canvas.pack()

# Buttons to control playback
btn = tkinter.Button(window, text='< - Previous - Fast', width=50,command = partial
(play, -25))
btn.pack()

btn = tkinter.Button(window, text='<< -- Previous - Slow', width=50, command =partial
(play, -2))
btn.pack()

btn = tkinter.Button(window, text='Next - Fast -- >>', width=50, command=partial
(play,25))
btn.pack()

btn = tkinter.Button(window, text='Next - Slow - >', width=50,command = partial
(play, 2))
btn.pack()

btn = tkinter.Button(window, text='Give OUT', width=50,command = out)
btn.pack()

btn = tkinter.Button(window, text='Give NOT-OUT', width=50,command = not_out)
btn.pack()

window.mainloop()
