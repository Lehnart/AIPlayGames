from typing import List

from tictactoe.ai_player import AIPlayer
from tictactoe.human_player import HumanPlayer
from tictactoe.state import State, GameStatus


class Logic:

    def __init__(self, state: State):
        self.state = state
        self.player1 = HumanPlayer()
        self.player2 = AIPlayer()

    def update(self, events: List):
        next_move = None
        if self.state.next_player == 0:
            next_move = self.player1.next_move(events)
        elif self.state.next_player == 1:
            next_move = self.player2.next_move(events)
        if next_move is not None:
            self.play(*next_move)

    def play(self, row: int, col: int):
        if self.state.game_status is not GameStatus.PLAYING:
            return
        if not self.is_case_allowed(row, col):
            return
        self.state.set_symbol(row, col)
        self.check_if_game_is_over()

    def check_if_game_is_over(self):
        if self.has_a_player_won():
            self.state.set_game_over_status(GameStatus.WON)
            self.state.set_winner(self.get_game_winner())
            print(f"Player {self.get_game_winner()} has won ")
            return True
        elif self.is_board_full():
            self.state.set_game_over_status(GameStatus.DRAW)
            print(f"It's a draw")
            return True
        return False

    def is_case_allowed(self, row, col):
        return self.state.get_symbol_in_case(row, col) is None

    def has_a_player_won(self):
        return self.get_symbol_winner() is not None

    def get_symbol_winner(self):
        lines = [
            [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]
        ]
        for line in lines:
            symbols = {}
            for row, col in line:
                symbol = self.state.get_symbol_in_case(row, col)
                if symbol is None:
                    continue
                if symbol not in symbols:
                    symbols[symbol] = 0
                symbols[symbol] += 1
            for symbol in symbols:
                if symbols[symbol] == 3:
                    return symbol

        return None

    def get_game_winner(self):
        symbol = self.get_symbol_winner()
        if symbol is None:
            return None
        return self.state.player_symbol.index(symbol)

    def is_board_full(self):
        for row in range(self.state.row_count):
            for col in range(self.state.col_count):
                if self.state.get_symbol_in_case(row, col) is None:
                    return False
        return True

    def is_game_over(self):
        return self.is_board_full() or self.has_a_player_won()
