from square import Square
from piece import *

class Board:
    def __init__(self):
        self.set_start_state()

    def set_start_state(self):
        self.board = []

        # Setting row 1 - white pieces
        row1 = [Square(Rook(PieceColor.white)), Square(Knight(PieceColor.white)), Square(Bishop(PieceColor.white)), Square(Queen(PieceColor.white)), Square(King(PieceColor.white)), Square(Bishop(PieceColor.white)), Square(Knight(PieceColor.white)), Square(Rook(PieceColor.white))]
        self.board.append(row1)

        # Setting row 2 - white pieces
        row2 = [Square(Pawn(PieceColor.white)), Square(Pawn(PieceColor.white)), Square(Pawn(PieceColor.white)), Square(Pawn(PieceColor.white)), Square(Pawn(PieceColor.white)), Square(Pawn(PieceColor.white)), Square(Pawn(PieceColor.white)), Square(Pawn(PieceColor.white))]
        self.board.append(row2)

        # Setting rows 3 to 6 - empty spaces
        row3to6 = [Square(None), Square(None), Square(None), Square(None), Square(None), Square(None), Square(None), Square(None)]
        for i in range(4):
            self.board.append(row3to6)

        # Setting row 7 - black pieces
        row7 = [Square(Pawn(PieceColor.black)), Square(Pawn(PieceColor.black)), Square(Pawn(PieceColor.black)), Square(Pawn(PieceColor.black)), Square(Pawn(PieceColor.black)), Square(Pawn(PieceColor.black)), Square(Pawn(PieceColor.black)), Square(Pawn(PieceColor.black))]
        self.board.append(row7)

        # Setting row 8 - black pieces
        row8 = [Square(Rook(PieceColor.black)), Square(Knight(PieceColor.black)), Square(Bishop(PieceColor.black)), Square(King(PieceColor.black)), Square(Queen(PieceColor.black)), Square(Bishop(PieceColor.black)), Square(Knight(PieceColor.black)), Square(Rook(PieceColor.black))]
        self.board.append(row8)

    def print_state(self):
        for i in range(8):
            print(8 - i, end = "  ")
            
            for j in range(8):
                square = self.board[8 - i - 1][j]
                if square.piece:
                    piece_type = square.piece.get_type()
                    piece_string = piece_type[0].value + "_" + piece_type[1]
                    whitespace_suffix = " "
                    # Figure out suffix
                    for k in range(12 - len(piece_string)):
                        whitespace_suffix = whitespace_suffix + " "
                    print(piece_string, end = whitespace_suffix)
                else:
                    print("      .", end = "      ")
            print()

        # Bruh make this better
        print()
        print("   a            b            c            d            e            f            g            h")


    # TODO: Add functions to update board state
        
