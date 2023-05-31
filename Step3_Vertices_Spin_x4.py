"""
Rotating Cube
Step 1 : Opening a window and displaying 1 vertex
Step 2 : Integrate the rotation function and matrix manipulation
Step 3 : Display 4 vertices with a very unoptimized code

Author : Matis Messence
20/04/2023

I am on a coding adventure to learn python, data science and machine learning.
Follow my progress at
https://www.linkedin.com/in/matis-messence/
https://github.com/MessenceM
"""

from tkinter import *
import numpy as np

SPEED = 50
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
v1 = np.array([[1], [1], [0]])
v2 = np.array([[1], [-1], [0]])
v3 = np.array([[-1], [-1], [0]])
v4 = np.array([[-1], [1], [0]])

CENTER = np.array([[200], [200], [0]])
angle = 0
Rx = np.matrix([[np.cos(angle), -np.sin(angle), 0],
                [np.sin(angle), np.cos(angle), 0],
                [0, 0, 1]])
ROT1 = np.matmul(Rx, v1)
ROT2 = np.matmul(Rx, v2)
ROT3 = np.matmul(Rx, v3)
ROT4 = np.matmul(Rx, v4)

PROJ1 = np.add(np.multiply(ROT1, 100), CENTER)
PROJ2 = np.add(np.multiply(ROT2, 100), CENTER)
PROJ3 = np.add(np.multiply(ROT3, 100), CENTER)
PROJ4 = np.add(np.multiply(ROT4, 100), CENTER)


def rotate():
    global Rx
    global angle
    Rx = np.matrix([[np.cos(angle), -np.sin(angle), 0],
                    [np.sin(angle), np.cos(angle), 0],
                    [0, 0, 1]])
    global ROT1
    global ROT2
    global ROT3
    global ROT4
    ROT1 = np.matmul(Rx, v1)
    ROT2 = np.matmul(Rx, v2)
    ROT3 = np.matmul(Rx, v3)
    ROT4 = np.matmul(Rx, v4)
    global PROJ1
    global PROJ2
    global PROJ3
    global PROJ4
    PROJ1 = np.add(np.multiply(ROT1, 100), CENTER)
    PROJ2 = np.add(np.multiply(ROT2, 100), CENTER)
    PROJ3 = np.add(np.multiply(ROT3, 100), CENTER)
    PROJ4 = np.add(np.multiply(ROT4, 100), CENTER)
    global POINT1
    global POINT2
    global POINT3
    global POINT4
    canvas.delete(POINT1)
    canvas.delete(POINT2)
    canvas.delete(POINT3)
    canvas.delete(POINT4)

    POINT1 = canvas.create_oval(int(PROJ1[0]) - 5, int(PROJ1[1]) - 5, int(PROJ1[0]) + 5, int(PROJ1[1]) + 5, width=0,
                                fill='white')
    POINT2 = canvas.create_oval(int(PROJ2[0]) - 5, int(PROJ2[1]) - 5, int(PROJ2[0]) + 5, int(PROJ2[1]) + 5, width=0,
                                fill='white')
    POINT3 = canvas.create_oval(int(PROJ3[0]) - 5, int(PROJ3[1]) - 5, int(PROJ3[0]) + 5, int(PROJ3[1]) + 5, width=0,
                                fill='white')
    POINT4 = canvas.create_oval(int(PROJ4[0]) - 5, int(PROJ4[1]) - 5, int(PROJ4[0]) + 5, int(PROJ4[1]) + 5, width=0,
                                fill='white')

    angle = angle + INCR
    print(Rx)
    canvas.after(SPEED, rotate)


POINT1 = canvas.create_oval(int(PROJ1[0]) - 5, int(PROJ1[1]) - 5, int(PROJ1[0]) + 5, int(PROJ1[1]) + 5, width=0,
                            fill='white')
POINT2 = canvas.create_oval(int(PROJ2[0]) - 5, int(PROJ2[1]) - 5, int(PROJ2[0]) + 5, int(PROJ2[1]) + 5, width=0,
                            fill='white')
POINT3 = canvas.create_oval(int(PROJ3[0]) - 5, int(PROJ3[1]) - 5, int(PROJ3[0]) + 5, int(PROJ3[1]) + 5, width=0,
                            fill='white')
POINT4 = canvas.create_oval(int(PROJ4[0]) - 5, int(PROJ4[1]) - 5, int(PROJ4[0]) + 5, int(PROJ4[1]) + 5, width=0,
                            fill='white')
rotate()
root.mainloop()
