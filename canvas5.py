import tkinter as tk
import random

window= tk.Tk()

canvas=tk.Canvas(window,width=500,height=500)
canvas.pack()

circle=canvas.create_oval(50,50,100,100, fill="blue")

def update_circle():
    x1,y1,x2,y2=canvas.coords(circle)
    dx=random.randint(-5,5)
    dy=random.randint(-5,5)
    canvas.move(circle,dx,dy)
    window.after(10,update_circle)


update_circle()

window.mainloop()