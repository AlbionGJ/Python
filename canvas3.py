import tkinter as tk

window= tk.Tk()

canvas=tk.Canvas(window,width=250,height=250)
canvas.pack()

photo= tk.PhotoImage(file="gif.rigolo.gif")

image=canvas.create_image(0,0,image=photo,anchor=tk.NW)

window.mainloop()