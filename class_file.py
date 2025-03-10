import pygame

# Defining colors which will be used later
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

    def update_current_score(self, cps):
        self.current_score += round(cps, 2)

    def reset_current_score(self):
        self.current_score = 0

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
        self.width = 85
        self.height = 45
        self.position = car_position
        self.speed = speed

        self.image = pygame.transform.scale(pygame.image.load("red-car-top-view-clipart.png"), (self.width, self.height))

    def reset_position(self):
        self.position = Position(0, 597)
        self.speed = 0

    # Displays a "car" on a defined surface at a defined position
    def draw(self, surface):
        surface.blit(self.image, (self.position.x, self.position.y))

# The Player class has a name attribute and a score attribute. An object of this class represents a player
class Player:
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    # User-friendly string representation of a Player object
    def __repr__(self):
        return "Player: {}, Score: {}".format(self.name, self.score)


# the button class it takes an image that we will use, creates a rectangle for the image and it also displays the position
class Start:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False

        # get mouse position
        position = pygame.mouse.get_pos()

        # check mouse over and clicked conditions
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action


class Time:
    def __init__(self, time = 5):
        self.time = time
        self.start_time = pygame.time.get_ticks()

    def update_time(self):
        time_passed = (pygame.time.get_ticks() - self.start_time) // 1000

        if time_passed >= 1:
            self.time -= time_passed
            self.start_time = pygame.time.get_ticks()
            if self.time < 0:
                self.time = 0

    def reset_timer(self):
        self.time = 5
        self.start_time = pygame.time.get_ticks()

    def draw(self, surface):
        font = pygame.font.SysFont("Comic Sans MS", 30)  # Creates a font object
        text_one = font.render("Time: {}".format(self.time), True, BLACK)  # Creates time text in the desired font
        surface.blit(text_one, (870, 10))  # Displays text on a defined surface



