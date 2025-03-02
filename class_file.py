import pygame
import main

# Defining colors which will later be used for displayed the car on the game screen.
RED = (250, 0 , 0)
BLACK = (0, 0, 0)


class Score:
    def __init__(self, high_score = 0, current_score = 0):
        self.high_score = high_score
        self.current_score = current_score

    def update_high_score(self, current_score):
        self.current_score = current_score
        if current_score > self.high_score:
            self.high_score = current_score

    # Need to add def update_current_score() to update the current score based on the clicker.

    def draw(self, surface):
        font = pygame.font.SysFont("Comic Sans MS", 35)
        text_one = font.render("High Score: {}".format(self.high_score), True, BLACK)
        text_two = font.render("Current Score: {}".format(self.current_score), True, BLACK)
        surface.blit(text_one, (10, 10))
        surface.blit(text_two, (10, 50))

class Position:
    def __init__(self, x_position: int , y_position: int ):
        self.x = x_position
        self.y = y_position


# The Car class has a car position attribute and speed attribute. It also has a width and a height. There is a
# move_car() function which is responsible for moving the car's x-position, and a draw() function which allows us
# to display the car on the game screen.

class Car:
    def __init__(self, car_position:Position, speed = 0):
        self.width = 50
        self.height = 30
        self.position = car_position
        self.speed = speed

    def move_car(self):
        self.position.x += self.speed

        if self.position.x + self.width > main.WIDTH:
            self.position.x = main.WIDTH - self.width

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.position.x, self.position.y, self.width, self.height))

class Player:
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score
