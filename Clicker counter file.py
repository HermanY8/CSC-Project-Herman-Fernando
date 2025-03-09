from tkinter import *
from threading import Timer

choose = input("How many seconds do you want?")
choose = int(choose)
turn = 0
cps = 0
num = 0

window = Tk()
window.geometry('800x600')



def cps2():
    global  num
    cps = num/choose
    cps = str(cps)
    print("Your CPS:" + cps)
    your_cps = Entry(window)
    your_cps.insert(END,"Your CPS:" + cps)
    your_cps.pack()


cpstrack = Timer(choose, cps2)


def addcps():
    global num
    num += 1

def runcps():
    global turn
    if turn == 1:
        addcps()
    if turn == 0:
        cpstrack.start()
        turn += 1
        Click_to_Start["text"] = "Click!"

Click_to_Start = Button(window, text = "Click to Start!", padx = 200, pady= 100, command=runcps)
Click_to_Start.pack()

window.mainloop()