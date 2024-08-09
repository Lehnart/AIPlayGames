import enum

from tictactoe.board import Board


class GameStatus(enum.Enum):
    PLAYING = 0
    DRAW = 1
    WON = 2


class State:

    def __init__(self):
        self.player_count = 2
        self.next_player: int = 0
        self.board = Board()
        self.player_symbol = ["X", "O"]
        self.game_status = GameStatus.PLAYING
        self.winner = None

    def play(self, row: int, col: int):
        self.board.set_symbol(row, col, self.get_current_symbol())
        self.next_player += 1
        self.next_player %= self.player_count

        if self.has_a_player_won():
            self.set_game_over_status(GameStatus.WON)
            self.set_winner(self.get_winner_index())
        elif self.is_board_full():
            self.set_game_over_status(GameStatus.DRAW)

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

    @staticmethod
    def clone(other_state):
        new_state = State()
        new_state.player_count = other_state.player_count
        new_state.next_player = other_state.next_player
        new_state.board = Board.clone(other_state.board)
        new_state.player_symbol = other_state.player_symbol
        new_state.game_status = other_state.game_status.PLAYING
        new_state.winner = other_state.winner
        return new_state

    def is_move_allowed(self, row, col):
        return self.board.get_symbol_in_case(row, col) is None

    def has_a_player_won(self):
        return self.get_winner_symbol() is not None

    def get_winner_symbol(self):
        lines = [
            [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]
        ]
        for line in lines:
            symbols = {}
            for row, col in line:
                symbol = self.board.get_symbol_in_case(row, col)
                if symbol is None:
                    continue
                if symbol not in symbols:
                    symbols[symbol] = 0
                symbols[symbol] += 1
            for symbol in symbols:
                if symbols[symbol] == 3:
                    return symbol

        return None

    def get_winner_index(self):
        symbol = self.get_winner_symbol()
        if symbol is None:
            return None
        return self.player_symbol.index(symbol)

    def is_board_full(self):
        for row in range(self.board.row_count):
            for col in range(self.board.col_count):
                if self.board.get_symbol_in_case(row, col) is None:
                    return False
        return True

    def is_game_round_over(self):
        if self.has_a_player_won():
            return True
        elif self.is_board_full():
            return True
        return False
