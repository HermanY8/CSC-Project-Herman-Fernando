

import pygame
import time
import random

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #Window Screen that we created
pygame.display.set_caption("Clicks") # The main at the top of the window of our game

BG = pygame.transform.scale(pygame.image.load("download (1).jpg"), (WIDTH, HEIGHT))

def draw():
    WIN.blit(BG, (0, 0))
    pygame.display.update()

# making a while loop to make sure that our window stays open
def main():
    run = True

    while run:
        for event in pygame.event.get(): # Looking at when user presses x-button to close window
            if event.type == pygame.QUIT:
                run = False # end for loop.
                break
        draw()



    pygame.quit() #closes window

if __name__ == "__main__": # makes sure we are running file and not importing it from a different file
    main()