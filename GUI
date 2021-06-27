from tkinter import *
import tkinter
import numpy as np

n = 10
d = 2

startgrid = np.zeros([n]*d)

window = Tk()
frame = Frame(window)
Grid.rowconfigure(window, 0, weight=1)
Grid.columnconfigure(window, 0, weight=1)
frame.grid(row=0, column=0, sticky=N+S+E+W)
grid = Frame(frame)
grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
Grid.rowconfigure(frame, 7, weight=1)
Grid.columnconfigure(frame, 0, weight=1)

een = "red"
nul = "white"

def click(btn, x, y):
    if btn["bg"] == een:
        btn["bg"] = nul
        startgrid[x,y] = 0
        print(startgrid)
    else:
        btn["bg"] = een
        startgrid[x,y] = 1
        print(startgrid)

def magie(lengte=10):
    for x in range(lengte):
        for y in range(lengte):
            btn = tkinter.Button(frame, bg=nul, text=str(x) + " " + str(y))
            btn.grid(column=y, row=x, sticky=N+S+E+W)
            btn["command"] = lambda btn=btn, x=x, y=y: click(btn, x, y)

    for x in range(lengte):
        Grid.columnconfigure(frame, x, weight=1)

    for y in range(lengte):
        Grid.rowconfigure(frame, y, weight=1)

    return frame

w = magie(10)

tkinter.mainloop()
