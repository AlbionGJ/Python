import tkinter 

window= tkinter.Tk()

canvas=tkinter.Canvas(window,width=500,height=500)
canvas.pack()

text=canvas.create_text(250,250,text="Hello World!")

window.mainloop()