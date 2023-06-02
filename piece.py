from enum import Enum

class PieceColor(Enum):
    black = "Black"
    white = "White"

class Piece:
    def __init__(self, color):
        self.color = color

class Pawn(Piece):
    def is_valid_move(self):
        pass

    def get_type(self):
        return (self.color, "pawn")

class Rook(Piece):
    def is_valid_move(self):
        pass

    def get_type(self):
        return (self.color, "rook")

class Knight(Piece):
    def is_valid_move(self):
        pass

    def get_type(self):
        return (self.color, "knight")

class Bishop(Piece):
    def is_valid_move(self):
        pass

    def get_type(self):
        return (self.color, "bishop")

class Queen(Piece):
    def is_valid_move(self):
        pass

    def get_type(self):
        return (self.color, "queen")

class King(Piece):
    def is_valid_move(self):
        pass

    def get_type(self):
        return (self.color, "king")
