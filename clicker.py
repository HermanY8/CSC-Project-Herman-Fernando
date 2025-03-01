from tkinter import *
from threading import Timer

window = Tk()

window.geometry("800x600")

ClickerStart = Button(window, text="Click To start", padx=200, pady=100)
ClickerStart.pack()
window.mainloop()