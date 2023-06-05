from piece import Piece

class Square:
    def __init__(self, piece, row, col):
        self.piece = piece
        self.row = row
        self.col = col
        self.matrix_row = self.row - 1
        self.matrix_col = ord(self.col) - 97

