"""
Rotating Cube
Step 1 : Opening a window and displaying 1 vertex

Author : Matis Messence
19/04/2023

I am on a coding adventure to learn python, data science and machine learning.
Follow my progress at
https://www.linkedin.com/in/matis-messence/
https://github.com/MessenceM
"""

from tkinter import *
import numpy as np

WIDTH = 400
HEIGHT = 400
CANVAS_MID_X = WIDTH/2
CANVAS_MID_Y = HEIGHT/2
SIDE = WIDTH/4

#window
WIDTH = 400
HEIGHT = 400
CANVAS_MID_X = WIDTH/2
CANVAS_MID_Y = HEIGHT/2
SIDE = WIDTH/2

root = Tk()
canvas = Canvas(root, bg="black", height=HEIGHT, width=WIDTH)
canvas.pack()

#numbers
angle = np.pi/2
v1 = np.array([[1], [0], [0]])
CENTER = np.array([[200], [200], [0]])

#rotation
Rx = np.matrix([[np.cos(angle), -np.sin(angle), 0],
                [np.sin(angle), np.cos(angle) , 0],
                [0            , 0            , 1]])
ROT1 = np.matmul(Rx, v1)
print('ROT1 =', ROT1)

#projection
PROJ1 = np.add(np.multiply(ROT1,100), CENTER)
print('PROJ1=', PROJ1)


canvas.create_oval(int(PROJ1[0])-5, int(PROJ1[1])-5, int(PROJ1[0])+5, int(PROJ1[1])+5, width = 0, fill = 'white')
root.mainloop()