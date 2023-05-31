from piece import Piece_Color

class Player:
    def __init__(self, piece_color):
        self.piece_color = piece_color

class Bot(Player):
    # TODO: Add model integration
    def make_move(self):
        pass

class Human(Player):
    # TODO: Take in user input
    def make_move(self):
        pass