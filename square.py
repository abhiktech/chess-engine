from piece import Piece

class Square:
    def __init__(self, piece):
        self.piece = piece

    def set_state(self, piece):
        self.piece = piece

    def set_empty(self):
        self.piece = None

    def is_empty(self):
        return self.piece == None
