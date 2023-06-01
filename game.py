from board import Board
from player import PlayerType, Player
from piece import PieceColor
from player import Bot, Human

class Game:
    def __init__(self):
        self.board = Board()
        self.player_white = None
        self.player_black = None
        self.current_player_piece_color = PieceColor.white
        self.is_game_running = True

    def run(self):
        print("Welcome to Abhik's chess engine!\n")
        player_white_type = Game.get_player_type(PieceColor.white.value)
        self.player_white = Game.get_player_object(PieceColor.white, player_white_type)
        player_black_type = Game.get_player_type(PieceColor.black.value)
        self.player_black = Game.get_player_object(PieceColor.black, player_black_type)

        while self.is_game_running:
            # TODO: How to figure out if game is over?
            if self.current_player_piece_color == PieceColor.white:
                self.player_white.make_move()
            else:
                self.player_black.make_move()
            self.is_game_running = False # TODO: Remove

        print("Player " + self.current_player_piece_color.value + " wins!")

    def get_player_type(player):
        input_prompt = f"Select Player {player} type : {PlayerType.human.value} {PlayerType.bot.value} : "
        player_type = input(input_prompt)
        while player_type not in (PlayerType.human.value, PlayerType.bot.value):
            player_type = input("Incorrect input! " + input_prompt)
        print()
        
        if player_type == PlayerType.human.value:
            return PlayerType.human
        elif player == PlayerType.bot.value:
            return PlayerType.bot

    def get_player_object(piece_color, player_type):
        if player_type == PlayerType.human:
            return Human(piece_color)
        elif player_type == PlayerType.bot:
            return Bot(piece_color)
        # TODO: Add more

