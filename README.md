Project Title: "Clicks"

Our project is a racing game in which a player controls a car's speed based on their
clicks per second. The high score and the current score are displayed on the screen.

main.py file:

This is the driver file. In this file, the Pygame window is created, instances of
Car and Score are created, and the game is ran until the x-button is pressed.

This file imports Pygame, which is a Python library with many functions
which are helpful for the creation of video games. In main.py, we are using the 
Pygame library for the graphics (displaying the background, car, and score). 

We also import class_file in order to use our Car and Score classes and their
respective methods. 

class_file file:

This file is used for all of our class definitions (along with their respective
methods). Here, we created the Score class, Position class, Car class, and Player
class. The Score class keeps track of current score and high score. The Position
class is used to keep track of an object's position on the screen. A Car class object 
is used to represent a car with position and speed. A Player class object represents
a player in the game with a name and a score.

Clicker counter file:

This file is used for our "clicker," which is what will be used to keep track of a player's 
clicks per second. These clicks per second of a player will determine a car's speed and
therefore a player's score. This is still a work in progress.

