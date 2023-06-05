from piece import *
from square import Square

class Board:
    def __init__(self):
        self.set_start_state()

    def set_start_state(self):
        self.matrix = []

        # Setting row 1 - white pieces
        row1 = [Square(Rook(PieceColor.white), 1, 'a'), Square(Knight(PieceColor.white), 1, 'b'), Square(Bishop(PieceColor.white), 1, 'c'), Square(Queen(PieceColor.white), 1, 'd'), Square(King(PieceColor.white), 1, 'e'), Square(Bishop(PieceColor.white), 1, 'f'), Square(Knight(PieceColor.white), 1, 'g'), Square(Rook(PieceColor.white), 1, 'h')]
        self.matrix.append(row1)

        # Setting row 2 - white pieces
        row2 = [Square(Pawn(PieceColor.white), 2, 'a'), Square(Pawn(PieceColor.white), 2, 'b'), Square(Pawn(PieceColor.white), 2, 'c'), Square(Pawn(PieceColor.white), 2, 'd'), Square(Pawn(PieceColor.white), 2, 'e'), Square(Pawn(PieceColor.white), 2, 'f'), Square(Pawn(PieceColor.white), 2, 'g'), Square(Pawn(PieceColor.white), 2, 'h')]
        self.matrix.append(row2)

        # Setting rows 3 to 6 - empty spaces
        cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for i in range(4):
            row = []
            for col in cols:
                row.append(Square(None, i + 3, col))
            self.matrix.append(row)

        # Setting row 7 - black pieces
        row7 = [Square(Pawn(PieceColor.black), 7, 'a'), Square(Pawn(PieceColor.black), 7, 'b'), Square(Pawn(PieceColor.black), 7, 'c'), Square(Pawn(PieceColor.black), 7, 'd'), Square(Pawn(PieceColor.black), 7, 'e'), Square(Pawn(PieceColor.black), 7, 'f'), Square(Pawn(PieceColor.black), 7, 'g'), Square(Pawn(PieceColor.black), 7, 'h')]
        self.matrix.append(row7)

        # Setting row 8 - black pieces
        row8 = [Square(Rook(PieceColor.black), 8, 'a'), Square(Knight(PieceColor.black), 8, 'b'), Square(Bishop(PieceColor.black), 8, 'c'), Square(King(PieceColor.black), 8, 'd'), Square(Queen(PieceColor.black), 8, 'e'), Square(Bishop(PieceColor.black), 8, 'f'), Square(Knight(PieceColor.black), 8, 'g'), Square(Rook(PieceColor.black), 8, 'h')]
        self.matrix.append(row8)

    def print_state(self):
        for i in range(8):
            print(8 - i, end = "  ")
            
            for j in range(8):
                square = self.matrix[8 - i - 1][j]
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


    
    
    def is_valid_move(i, n):
        pass

    # TODO: Add functions to update board state
        
