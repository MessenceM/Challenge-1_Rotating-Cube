"""
Rotating Cube
Step 1 : Opening a window and displaying 1 vertex
Step 2 : Integrate the rotation function and matrix manipulation

Author : Matis Messence
20/04/2023

I am on a coding adventure to learn python, data science and machine learning.
Follow my progress at
https://www.linkedin.com/in/matis-messence/
https://github.com/MessenceM
"""

from tkinter import *
import numpy as np

SPEED = 30
RES = 100
INCR = 2 * np.pi / RES

WIDTH = 400
HEIGHT = 400
CANVAS_MID_X = WIDTH / 2
CANVAS_MID_Y = HEIGHT / 2
SIDE = WIDTH / 4

# window
WIDTH = 400
HEIGHT = 400
CANVAS_MID_X = WIDTH / 2
CANVAS_MID_Y = HEIGHT / 2
SIDE = WIDTH / 2

root = Tk()
root.title('Im turning around !')
canvas = Canvas(root, bg="black", height=HEIGHT, width=WIDTH)
canvas.pack()

# numbers
v1 = np.array([[1], [0], [0]])
CENTER = np.array([[200], [200], [0]])
angle = 0
Rx = np.matrix([[np.cos(angle), -np.sin(angle), 0],
                [np.sin(angle), np.cos(angle), 0],
                [0, 0, 1]])
ROT1 = np.matmul(Rx, v1)
PROJ1 = np.add(np.multiply(ROT1, 100), CENTER)


def rotate():
    global Rx
    global angle
    Rx = np.matrix([[np.cos(angle), -np.sin(angle), 0],
                    [np.sin(angle), np.cos(angle), 0],
                    [0, 0, 1]])
    global ROT1
    ROT1 = np.matmul(Rx, v1)
    global PROJ1
    PROJ1 = np.add(np.multiply(ROT1, 100), CENTER)
    global POINT
    canvas.delete(POINT)
    POINT = canvas.create_oval(int(PROJ1[0]) - 5, int(PROJ1[1]) - 5, int(PROJ1[0]) + 5, int(PROJ1[1]) + 5, width=0,
                       fill='white')
    angle = angle + INCR
    print(Rx)
    canvas.after(SPEED, rotate)


POINT = canvas.create_oval(int(PROJ1[0]) - 5, int(PROJ1[1]) - 5, int(PROJ1[0]) + 5, int(PROJ1[1]) + 5, width=0,
                           fill='white')
rotate()
root.mainloop()
