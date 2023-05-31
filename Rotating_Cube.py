"""
Rotating Cube
Step 1 : Opening a window and displaying 1 vertex
Step 2 : Integrate the rotation function and matrix manipulation
Step 3 : Display 4 vertices with a very unoptimized code
Step 4 : Add a second rotation axis and clean the mess
Step 5 : Display 8 vertices, add the links lines between them and add a 3rd rotation

Author : Matis Messence
22/04/2023

I am on a coding adventure to learn python, data science and machine learning.
Follow my progress at
https://www.linkedin.com/in/matis-messence/
https://github.com/MessenceM
"""

from tkinter import *
import numpy as np

speed = 50
res = 100
incr = 2 * np.pi / res

# window
width = 400
height = 400
canvas_mid_X = width / 2
canvas_mid_Y = height / 2
side = width / 2

root = Tk()
root.title('Im turning around !')
canvas = Canvas(root, bg="black", height=height, width=width)
canvas.pack()

# vertices
v1 = np.array([1, 1, 1])
v2 = np.array([1, -1, 1])
v3 = np.array([-1, -1, 1])
v4 = np.array([-1, 1, 1])
v5 = np.array([1, 1, -1])
v6 = np.array([1, -1, -1])
v7 = np.array([-1, -1, -1])
v8 = np.array([-1, 1, -1])
vertices = np.array([v1, v2, v3, v4, v5, v6, v7, v8])
center = np.array([[200], [200]])


def rotate():
    global Xangle
    global Yangle
    global Zangle
    P = np.matrix('100 0 0; 0 100 0')
    Rx = np.matrix([[np.cos(Xangle), -np.sin(Xangle), 0],
                    [np.sin(Xangle), np.cos(Xangle), 0],
                    [0, 0, 1]]).T

    Ry = np.matrix([[np.cos(Yangle), 0, np.sin(Yangle)],
                    [0, 1, 0],
                    [-np.sin(Yangle), 0, np.cos(Yangle)]]).T
    Rz = np.matrix([[1, 0, 0],
                    [0, np.cos(Zangle), -np.sin(Zangle)],
                    [0, np.sin(Zangle), np.cos(Zangle)]]).T

    vertices_ROT_X = np.matmul(Rx, vertices.T)
    vertices_ROT_Y = np.matmul(Ry, vertices_ROT_X)
    vertices_ROT_Z = np.matmul(Rz, vertices_ROT_Y)

    proj = np.matmul(P, vertices_ROT_Y) + center

    canvas.delete("all")
    rows, cols = proj.shape
    for col in range(cols):
        coord_left = proj[:, col] - 5
        coord_right = proj[:, col] + 5
        canvas.create_oval(int(coord_left[0]), int(coord_left[1]), int(coord_right[0]), int(coord_right[1]), width=0,
                           fill='white')
    for i in range(4):
        a = proj[0, i]
        b = proj[1, i]
        c = proj[0, (i+1) % 4]
        d = proj[1, (i+1) % 4]
        e = proj[0, i+4]
        f = proj[1, i+4]
        g = proj[0, ((i+1) % 4)+4]
        h = proj[1, ((i+1) % 4)+4]
        canvas.create_line(int(a), int(b), int(c), int(d), width=2, fill='white')
        canvas.create_line(int(e), int(f), int(g), int(h), width=2, fill='white')
        canvas.create_line(int(a), int(b), int(e), int(f), width=2, fill='white')
        canvas.create_line(int(c), int(d), int(g), int(h), width=2, fill='white')
    Xangle = Xangle + incr
    Yangle = Yangle + incr
    Zangle = Zangle + incr

    canvas.after(speed, rotate)

Xangle = 0
Yangle = 0
Zangle = 0
rotate()
root.mainloop()
