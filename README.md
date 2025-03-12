Project Title: "Clicks"

Our project is a racing game in which a player competes to get the highest score based
on their clicks per second. 

To start playing, press the start button. You can move the car by pressing the space bar.
The score will only increase if the space bar is pressed and let go, not if it is held down. 

This is a game of speed! Once the timer runs out, it's game over! Press the reset
button to test your skills again and see if you are able to get the high score!

main.py file:

This is the driver file. In this file, the Pygame window is created, instances of
Car and Score are created, and the game is run until the x-button is pressed.

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
is used to represent a car with position and speed. The Button class is used to keep
track of clicks on the start button and restart button. The Time class handles everything
related to time.


CREDIT FOR IMAGES USED 
Race_Track.png by hiten66 
https://stock.adobe.com/search?k=pixel+art+car&asset_id=968221098

intro_background.jpg by ad_stock
https://stock.adobe.com/search?k=pixel+mountain+background&asset_id=698684223

New Start Button.png by @Shlavs
https://www.pixilart.com/art/start-buttonpixil-c92085e91d246b9

red-car-top-view-clipart.png by ANoymous user
https://nohat.cc/f/race-car-clipart-car-clipart-top-view/m2i8K9H7K9m2b1i8-201907240501.html

Restart.png by Kapper24
https://www.pixilart.com/art/restart-button-cfbcd4336297cdd