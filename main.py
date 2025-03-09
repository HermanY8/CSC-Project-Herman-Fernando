import pygame
import time
import random
from tkinter import *
from threading import Timer
import class_file
from class_file import Score

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Window Screen that we created
pygame.display.set_caption("Clicks") # The main at the top of the window of our game

pygame.init() # Initializes Pygame modules which will be used in our program

BG = pygame.transform.scale(pygame.image.load("Race_Track.jpg"), (WIDTH, HEIGHT))  # Scaling background image to fit on the screen



velocity_of_car = .5 # This is the amount of space the car covers per click

turn = 0
cps = 0
num = 0


def cps2():
    global  num
    cps = num/class_file.Time().time
    cps = str(cps)
    print("Your CPS:" + cps)
    your_cps = Entry(WIN)
    your_cps.insert(END,"Your CPS:" + cps)
    your_cps.pack()


cpstrack = Timer(class_file.Time().time, cps2)


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

#for the click start the isssue is the Window. it might be becasue were using the wrong function
Click_to_Start = Button(WIN, text = "Click to Star!", padx = 200, pady= 100, command=runcps)
Click_to_Start.pack()









#sizes down the image used as the button because it was too big
start_img = pygame.image.load("New Start Button.png").convert_alpha()









#calls the button class in order to give its position/ its instance
start_button = class_file.Start(370,200, start_img, 0.2)

def draw(car, score, set_time):
    WIN.blit(BG, (0, 0))  # Draws the background image at coordinates (0, 0) (top left) on the game window

    car.draw(WIN)  # Displays the car object on the game window
    score.draw(WIN)  # Displays the high score and current score on the game window
    set_time.draw(WIN) # Displays the time in the window
    if start_button.draw(WIN):
        print("START")
        

    # Displays the start button in the window
    pygame.display.update() # Shows any changes made to the window display






def main():

    car = class_file.Car(class_file.Position(0, 605)) # Creates Car object at the defined position
    score = class_file.Score()  # Creates a Score object
    time = class_file.Time()

    run = True

    # Making a while loop to make sure that our window stays open and the game runs unless the x-button is pressed
    while run:
        # Looking at when user presses x-button to close window



        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        if keys [pygame.K_SPACE] and car.position.x + velocity_of_car + car.width <= WIDTH:
            car.position.x += velocity_of_car

            
        draw(car, score, time)

    pygame.quit() # Shuts down all Pygame modules and closes window

if __name__ == "__main__": # makes sure we are running file and not importing it from a different file
    main()