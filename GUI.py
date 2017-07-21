# GUI for project Pegasus

import tkinter
import time
import math
top = tkinter.Tk()

Canvas = tkinter.Canvas(top, bg="grey", height=1920, width=1080)
coord = 20, 20, 380, 200
track = Canvas.create_oval(coord, width=15)
Canvas.pack()

racecar = Canvas.create_oval(20, 20, 30, 30, outline='white', fill='blue')

for i in range(0,360):
    angle = i
    x = math.cos(math.radians(angle))
    y = math.sin(math.radians(angle))
    time.sleep(0.025)
    Canvas.move(racecar, x, y)
    Canvas.update()



top.mainloop();
