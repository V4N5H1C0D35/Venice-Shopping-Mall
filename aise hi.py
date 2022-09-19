import tkinter
from tkinter import *
root=Tk()
root.title("Welcome")
root.geometry("5090x6000")
root.configure(bg="black")
background_image=PhotoImage(file="front2.png")
background_label=Label(root,image=background_image)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
root.after(5009,root.destroy)
root.mainloop()

