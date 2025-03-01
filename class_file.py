import pygame
import main


class Score:
    def __int__(self, high_score:int , current_score:int, scores:int):
        self.HighScore = high_score
        self.Current_Score = current_score
        self.Scores = scores

class Position:
    def __int__(self, x_position: int , y_position: int ):
        self.x = x_position
        self.y = y_position


# The Car class has a car position attribute and speed attribute. It also has a length and width. There is a
# move_car() function which is responsible for moving the car's x-position, and a draw() function which allows us
# to display the car on the game screen.

# Defining colors which will later be used for displayed the car on the game screen.
RED = (250, 0 , 0)
BLACK = (0, 0, 0)

class Car :
    def __init__(self, car_position:Position, speed = 0):
        self.width = 80
        self.height = 30
        self.position = car_position
        self.speed = speed

    def move_car(self):
        self.position.x += self.speed

        if self.position.x + self.width > main.WIDTH:
            self.position.x = main.WIDTH - self.width

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.position.x, self.position.y, self.width, self.height))