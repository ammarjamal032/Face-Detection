from tkinter import *
from face_recognition import recognize
# Fucntion will run by pressing datasets button..
from face_detect import detect
from face_datasets import face_datasets
from training import train
import cv2, time

window = Tk()

window.wm_title("Face Recognition System")

l1 = Label(window, text = "Face Recognition System", font = "100")
l1.grid(row = 0, column = 0, rowspan = 2, columnspan = 2)

b1 = Button(window, text="Detect", width=15, height=5, font='50', command=detect)
#b1.grid(row = 6, column = 1)
b1.grid(row = 4, column = 0)

b2 = Button(window, text= "Datasets", width = 15, height = 5, font = "50", command = face_datasets)
#b2.grid(row = 4, column = 0)
b2.grid(row = 4, column = 1)

b1 = Button(window, text = "Train", width = 15, height = 5, font = "50", command = train)
#b1.grid(row = 4, column = 1)
b1.grid(row = 6, column = 0)

b2 = Button(window, text= "Recognize", width = 15, height = 5, font = "50", command = recognize)
#b2.grid(row = 6, column = 0)
b2.grid(row = 6, column = 1)

b3 = Button(window, text = "Close", width = 15, height = 5, font = "50",  command = window.destroy)
b3.grid(row = 8, column = 0)


window.mainloop()
