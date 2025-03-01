
class Score:
    def __int__(self, high_score:int , current_score:int, scores:int):
        self.HighScore = high_score
        self.Current_Score = current_score
        self.Scores = scores

class Position:
    def __int__(self, x_position: int , y_position: int ):
        self.x = x_position
        self.y = y_position

class Car :
    def __init__(self, length:int, width:int):
        self.length = length
        self.width = width
