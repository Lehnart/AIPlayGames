import enum

from tictactoe.board import Board


class GameStatus(enum.Enum):
    PLAYING = 0
    DRAW = 1
    WON = 2


class State:

    def __init__(self):
        self.player_count = 2
        self.next_player: int = 1
        self.board = Board()
        self.player_symbol = ["X", "O"]
        self.game_status = GameStatus.PLAYING
        self.winner = None

    def play(self, row: int, col: int):
        self.board.set_symbol(row, col, self.get_current_symbol())
        self.next_player += 1
        self.next_player %= self.player_count

    def get_current_symbol(self):
        return self.player_symbol[self.next_player]

    def set_game_over_status(self, status: GameStatus):
        self.game_status = status

    def set_winner(self, winner: int):
        self.winner = winner

    def reset(self):
        self.player_count = 2
        self.next_player: int = 0
        self.board = Board()
        self.player_symbol = ["X", "O"]
        self.game_status = GameStatus.PLAYING
        self.winner = None
