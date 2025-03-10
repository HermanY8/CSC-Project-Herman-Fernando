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

BG = pygame.transform.scale(pygame.image.load("Race_Track.jpg"), (WIDTH, HEIGHT))  # Scaling background image to fit on the screen

#sizes down the image used as the button because it was too big
start_img = pygame.image.load("New Start Button.png").convert_alpha()

velocity_of_car = .7 # This is the amount of space the car covers per click

cps = 0 # Clicks per second
num = 0 # Number of clicks

game_started = False  # Used to keep track of whether the game has started or not
last_time = pygame.time.get_ticks()  # Stores the time in ms

# Updates the score based on the amount of clicks per second
def cps2(score, time_left):
    global  cps, num, last_time
    if time_left > 0:  # Makes sure there is still time left on the timer
        # Calculates the time difference between calls of pygame.time.get_ticks()
        current_time = pygame.time.get_ticks()
        time_diff = (current_time - last_time) // 1000.0

        # If the time difference is 1 second (1 second has passed), then calculate the CPS, set last_time to current_time,
        # and update current score/high score accordingly
        if time_diff >= 1:
            cps = num / time_diff
            cps = int(cps)
            last_time = current_time
            score.update_current_score(cps)
            score.update_high_score(score.current_score)
            num = 0
    else:
        pass

# Increases the number of clicks by 1
def addcps():
    global num
    num += 1



#sizes down the image used as the button because it was too big
start_img = pygame.image.load("New Start Button.png").convert_alpha() # the start button image
restart_image = pygame.image.load("Restart.png").convert_alpha() # the restart button image

#calls the button class in order to give its position/ its instance for both the start and restart image
start_button = class_file.Button(370, 200, start_img, 0.2)
restart_button = class_file.Button(350, 288, restart_image, 0.3)


def draw(car, score, game_time):
    global game_started
    WIN.blit(BG, (0, 0))  # Draws the background image at coordinates (0, 0) (top left) on the game window

    car.draw(WIN)  # Displays the car object on the game window
    score.draw(WIN)  # Displays the high score and current score on the game window
    game_time.draw(WIN) # Displays the time in the window

    # Checks if start button has been pressed, it has been pressed it removes it from the window
    if not game_started:
        if start_button.draw(WIN):
            print("START")
            score.reset_current_score()
            game_started = True
            game_time.reset_timer()
            car.reset_position()

    if game_started and game_time.time == 0:
        if restart_button.draw(WIN):
            print("RESTART")
            game_started = False
            car.reset_position()



    # Displays the start button in the window
    pygame.display.update() # Shows any changes made to the window display


def main():
    global last_time, game_started

    car = class_file.Car() # Creates Car object
    score = class_file.Score()  # Creates a Score object
    game_time = class_file.Time()  # Creates a time object

    run = True

    # Making a while loop to make sure that our window stays open and the game runs unless the x-button is pressed
    while run:
        # Looking at when user presses x-button to close window

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if game_started and game_time.time > 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and car.position.x != WIDTH - car.width:
                        addcps()

        draw(car, score, game_time)

        keys = pygame.key.get_pressed()
        if game_started and game_time.time > 0:
            if keys [pygame.K_SPACE] and car.position.x + velocity_of_car + car.width <= WIDTH:
                car.position.x += velocity_of_car

        if game_started:
            cps2(score, game_time.time)
            game_time.update_time()

        if time.time == 0:
            pass

    pygame.quit() # Shuts down all Pygame modules and closes window

if __name__ == "__main__": # makes sure we are running file and not importing it from a different file
    main()