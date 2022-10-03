#make a digital clock in python and center it on the screen
from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.resizable(0, 0)

screen_width = root.winfo_screenwidth()
screen_height =  root.winfo_screenmmheight()

def tempo():
    string = strftime('%H:%M:%S')
    label.config(text = string)
    label.after(1000, tempo)

label = Label(root, font = ('ds-digital', 80), background = '#34B8FF', foreground= '#33B8FF', width= 400)
label.pack()
tempo()

width = 400
heigth = 110

posx = screen_width/2 - 150
posy = screen_height + 125    
root.geometry('%dx%d+%d+%d' %(width,heigth,posx,posy))

root.overrideredirect(True)

root.attributes('-topmost', 0)

root.attributes('-transparentcolor', '#34B8FF')

mainloop()