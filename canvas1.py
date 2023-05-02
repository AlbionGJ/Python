import tkinter as tk

window=tk.Tk()

canvas=tk.Canvas(window,width=500,height=500)
canvas.pack()

line=canvas.create_line(0,0,500,500)
rectangle=canvas.create_rectangle(50,50,250,250)
circle=canvas.create_oval(100,100,200,200)
polygon=canvas.create_polygon(300,350,400,450,450,460)

window.mainloop()
