from tkinter import *
from tkinter.ttk import *
from time import strftime 

dk = Tk()
dk.title("Clock")
dk.minsize(width=610,height=110)
dk.maxsize(width=600,height=100)

label = Label(dk, font=("ds-digital",80),background="black",foreground='white')
label.pack(anchor='center')

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000,time)

time()

dk.mainloop()