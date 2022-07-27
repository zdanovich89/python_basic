from tkinter import *
import random
import time


def roll():
    x = random.choice(['1.png', '2.png', '3.png', '4.png', '5.png', '6.png'])
    return x


def img(event):
    global d1, d2
    for i in range(18):
        d1 = PhotoImage(file=roll())
        d2 = PhotoImage(file=roll())
        lab1['image'] = d1
        lab2['image'] = d2
        root.update()
        time.sleep(0.12)


root = Tk()
root.geometry('1000x508')
root.title('Roll the dice!')
root.resizable(height=False, width=False)
root.iconphoto(True, PhotoImage(file='5.png'))
font = PhotoImage(file='table.png')
Label(root, image=font).pack()
lab1 = Label(root)
lab1.place(relx=0.3, rely=0.5, anchor=CENTER)
lab2 = Label(root)
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)
root.bind('<1>', img)
Button(root, text='Go', command=img('event')).pack()
root.mainloop()