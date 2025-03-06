import pygame
import time
import random
from tkinter import *
from threading import Timer
import class_file

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Window Screen that we created
pygame.display.set_caption("Clicks") # The main at the top of the window of our game

pygame.init() # Initializes Pygame modules which will be used in our program

# Scaling background image to fit on the screen
BG = pygame.transform.scale(pygame.image.load("Race_Track.jpg"), (WIDTH, HEIGHT))

def draw(car, score):
    WIN.blit(BG, (0, 0))

    # add every draw() from each class in here
    car.draw(WIN)
    score.draw(WIN)

    pygame.display.update()

# making a while loop to make sure that our window stays open
def main():

    car = class_file.Car(class_file.Position(0, 605))
    score = class_file.Score()

    run = True

    while run:
        for event in pygame.event.get(): # Looking at when user presses x-button to close window
            if event.type == pygame.QUIT:
                run = False # end for loop.
                break
        draw(car, score)


    pygame.quit() #closes window

if __name__ == "__main__": # makes sure we are running file and not importing it from a different file
    main()