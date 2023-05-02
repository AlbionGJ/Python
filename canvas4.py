import tkinter as tk

window= tk.Tk()

canvas=tk.Canvas(window,width=500,height=500)
canvas.pack()

circle=canvas.create_oval(50,50,100,100, fill="blue")

def update_circle():
    canvas.move(circle, 10, 0,)
    window.after(50,update_circle)
update_circle()

window.mainloop()