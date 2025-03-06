import pygame
import main

# Defining colors which will later be used for displayed the car on the game screen.
RED = (250, 0 , 0)
BLACK = (0, 0, 0)


# The Score class keeps track of a player's high score and current score and updates them accordingly. There is also a draw() method which
# is responsible for displaying the scores on the game window.
class Score:
    def __init__(self, high_score = 0, current_score = 0):
        self.high_score = high_score
        self.current_score = current_score

    def update_high_score(self, current_score):
        self.current_score = current_score
        if current_score > self.high_score:
            self.high_score = current_score

    # Need to work on this function
    # def update_current_score(self, current_score):
    #    return self.current_score += 1

    # This draw method displays the score information on the game window.
    def draw(self, surface):
        font = pygame.font.SysFont("Comic Sans MS", 30)  # Creates a font object
        text_one = font.render("High Score: {}".format(self.high_score), True, BLACK)  # Creates text in the desired font
        text_two = font.render("Current Score: {}".format(self.current_score), True, BLACK)  # Creates text in the desired font
        surface.blit(text_one, (10, 10))  # Displays text on a defined surface
        surface.blit(text_two, (10, 50))  # Displays text on a defined surface


# The Position class defines an object's x and y positions on the game window.
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
        self.position.x += self.speed  # Moves the car's x-position by adding the speed to it
        # Doesn't allow the car to move past the edge of the screen
        if self.position.x + self.width > main.WIDTH:
            self.position.x = main.WIDTH - self.width

    # Displays a red rectangle on a defined surface at a defined position
    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.position.x, self.position.y, self.width, self.height))


# The Player class has a name attribute and a score attribute. An object of this class represents a player
class Player:
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    # User-friendly string representation of a Player object
    def __repr__(self):
        return "Player: {}, Score: {}".format(self.name, self.score)


class Start:
    def __init__(self, x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        main.WIN.blit(self.image, (self.rect.x ,self.rect.y))

