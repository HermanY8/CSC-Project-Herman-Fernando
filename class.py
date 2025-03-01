from tkinter import *
class Score:
    def __int__(self, top_five:list[dict] , current_score:int, scores:int):
        self.top_five = []
        self.current_score = 0
        self.Scores = scores



class Position:
    def __int__(self, x_position: int , y_position: int ):
        self.x = x_position
        self.y = y_position

class Car :
    def __init__(self, length:int, width:int):
        self.length = length
        self.width = width

class Player :
    def __init__(self, name : str , total_score :int):
        self.name = name
        self.total_score = total_score
