import pygame
import time
import random
from tkinter import *
from threading import Timer


import class_file

root = Tk()
root.title("Clicks")
root.geometry("1000x800")
canvas = Canvas( root , width= 1000 , height= 800)
canvas.pack()



WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Window Screen that we created
pygame.display.set_caption("Clicks") # The main at the top of the window of our game

pygame.init() # Initializes Pygame modules which will be used in our program

BG = pygame.transform.scale(pygame.image.load("Race_Track.jpg"), (WIDTH, HEIGHT))  # Scaling background image to fit on the screen



set_time = 10
num = 0
timer = None

your_cps = Entry(root)
your_cps.pack()


def cps2():
    global num, choose, your_cps
    cps = num / choose
    your_cps.delete(0,END)
    your_cps.insert(END, f"Your CPS: {cps:.2f}")
    print("Your CPS:" + cps)

def addcps():
    global num
    num += 1


def runcps():
    global timer, num
    num = 0
    timer = Timer(choose, cps2)
    timer.start
Click_to_start = Button(root, text = "Click to Star!", padx = 200, pady= 100, command=runcps)
Click_to_start.pack()




def draw(car, score):
    WIN.blit(BG, (0, 0))  # Draws the background image at coordinates (0, 0) (top left) on the game window

    car.draw(WIN)  # Displays the car object on the game window
    score.draw(WIN)  # Displays the high score and current score on the game window

    pygame.display.update() # Shows any changes made to the window display

def main():

    car = class_file.Car(class_file.Position(0, 605)) # Creates Car object at the defined position
    score = class_file.Score()  # Creates a Score object

    run = True

    # Making a while loop to make sure that our window stays open and the game runs unless the x-button is pressed
    while run:
        # Looking at when user presses x-button to close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw(car, score)

    pygame.quit() # Shuts down all Pygame modules and closes window

if __name__ == "__main__": # makes sure we are running file and not importing it from a different file
    main()