from enum import Enum
from piece import PieceColor
from board import Board

class PlayerType(Enum):
    human = "human"
    bot = "bot"
    # TODO: Add more

class Player:
    def __init__(self, piece_color):
        self.piece_color = piece_color

class Bot(Player):
    # TODO: Add model integration
    def get_move(self, board, player_turn_piece_color):
        pass

    def make_move(self, board, player_turn_piece_color):
        return board

class Human(Player):

    def is_input_format_valid(position):
        if not position:
            return False
        
        if len(position) != 2:
            return False

        if ord(position[0]) < 97 or ord(position[0]) > 104:
            return False
        
        if ord(position[1]) < 49 or ord(position[1]) > 56:
            return False
        
        return True
    
    def get_input(player_turn_piece_color):
        initial_position = None
        new_position = None

        while not Human.is_input_format_valid(initial_position) or not Human.is_input_format_valid(new_position):
            input_prompt = f"Player {player_turn_piece_color.value}'s turn : "
            turn_input = input(input_prompt)
            # TODO: Handle case where less than 2 positions are entered due to which split() throws error
            [initial_position, new_position] = turn_input.split()
        return initial_position, new_position

    def is_valid_move(self, board, player_turn_piece_color, initial_square, new_square):
        # TODO: Add code to validate move
        return True

    def get_move(self, board, player_turn_piece_color):
        initial_position, new_position = Human.get_input(player_turn_piece_color)
        
        initial_square = board.matrix[int(initial_position[1]) - 1][ord(initial_position[0]) - 97]
        new_square = board.matrix[int(new_position[1]) - 1][ord(new_position[0]) - 97]

        while not self.is_valid_move(board, player_turn_piece_color, initial_square, new_square):
            initial_position, new_position = Human.get_input(player_turn_piece_color)
            initial_square = board.matrix[int(initial_position[1]) - 1][ord(initial_position[0]) - 97]
            new_square = board.matrix[int(new_position[1]) - 1][ord(new_position[0]) - 97]
        print()

        return initial_square, new_square


    
    def make_move(self, board, player_turn_piece_color):
        initial_square, new_square = self.get_move(board, player_turn_piece_color)
        board.matrix[new_square.matrix_row][new_square.matrix_col].piece = initial_square.piece
        board.matrix[initial_square.matrix_row][initial_square.matrix_col].piece = None 
        return board
