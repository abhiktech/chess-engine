from enum import Enum

class Piece_Color(Enum):
    black = 1
    white = 2

class Piece:
    def __init__(self, color):
        self.color = color

class Pawn(Piece):
    def is_valid_move(self):
        pass

class Rook(Piece):
    def is_valid_move(self):
        pass

class Knight(Piece):
    def is_valid_move(self):
        pass

class Bishop(Piece):
    def is_valid_move(self):
        pass

class Queen(Piece):
    def is_valid_move(self):
        pass

class King(Piece):
    def is_valid_move(self):
        pass
