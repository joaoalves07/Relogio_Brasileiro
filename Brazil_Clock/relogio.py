from tkinter import *
import tkinter
from datetime import datetime
import pytz
import time
import pyglet
pyglet.options['win32_gdi_font'] = True
pyglet.font.add_file("D:\VsCode\Python\Brazil_Clock\digital-7.ttf") #Folder where the font is located.

# setup colors and variables
white = "#F2F0F0"
blue = "#485673"

bg = white
txt = blue

# Creating empty window
window = Tk()
window.title("")
window.geometry("600x250")


# creating a def with the info i need

def clock():
    home = pytz.timezone('Brazil/East')
    time = datetime.now(home)
    hour = time.strftime("%H:%M:%S")

    # Config Labels
    l1.config(text='Brasília')
    l1.place(x=30, y=5)
    l2.config(text=hour,)
    l2.after(200, clock)
    l2.place(x=36, y=40)


def clock2():
    home2 = pytz.timezone('Brazil/Acre')
    time = datetime.now(home2)
    hour = time.strftime("%H:%M:%S")

    # Config Labels
    l3.config(text='Acre')
    l3.place(x=330, y=5)
    l4.config(text=hour,)
    l4.after(200, clock2)
    l4.place(x=317, y=40)


def clock3():
    home3 = pytz.timezone('Brazil/West')
    time = datetime.now(home3)
    hour = time.strftime("%H:%M:%S")

    # Config Labels
    l5.config(text='Amazonas')
    l5.place(x=25, y=105)
    l6.config(text=hour,)
    l6.after(200, clock3)
    l6.place(x=36, y=140)


def clock4():
    home4 = pytz.timezone('Brazil/DeNoronha')
    time = datetime.now(home4)
    hour = time.strftime("%H:%M:%S")

    # Config Labels
    l7.config(text='F. De Noronha')
    l7.place(x=280, y=105)
    l8.config(text=hour,)
    l8.after(200, clock4)
    l8.place(x=317, y=140)


# Creating the labels (clock)
l1 = Label(window, font=("digital-7 20"), bg=bg, fg=txt)
l2 = Label(window, font=("digital-7 20"), bg=bg, fg=txt)

# Creating the labels (clock2)
l3 = Label(window, font=("digital-7 20"), bg=bg, fg=txt)
l4 = Label(window, font=("digital-7 20"), bg=bg, fg=txt)

# Creating the labels (clock3)
l5 = Label(window, font=("digital-7 20"), bg=bg, fg=txt)
l6 = Label(window, font=("digital-7 20"), bg=bg, fg=txt)


# Creating the labels (clock4)
l7 = Label(window, font=("digital-7 20"), bg=bg, fg=txt)
l8 = Label(window, font=("digital-7 20"), bg=bg, fg=txt)


clock()
clock2()
clock3()
clock4()


window.mainloop()
