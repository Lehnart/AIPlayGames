from typing import List, Optional, Tuple


class State:

    def __init__(self):
        self.player_count = 2
        self.row_count = 3
        self.col_count = 3
        self.next_player: int = 0
        self.grid: List[List[Optional[str]]] = self.init_grid()
        self.player_symbol = ["X", "O"]
        self.is_game_over = False

    def init_grid(self):
        return [[None for _ in range(self.col_count)] for _ in range(self.row_count)]

    def set_symbol(self, row: int, col: int):
        self.grid[row][col] = self.get_current_symbol()
        self.next_player += 1
        self.next_player %= self.player_count

    def get_current_symbol(self):
        return self.player_symbol[self.next_player]

    def get_symbol_in_case(self, row: int, col: int):
        return self.grid[row][col]

    def get_cases_with_symbols(self) -> List[Tuple[int, int, str]]:
        symbols = []
        for i in range(self.row_count):
            for j in range(self.col_count):
                symbol = self.get_symbol_in_case(i, j)
                if symbol is not None:
                    symbols.append((i, j, symbol))

        return symbols

    def set_game_over_status(self, status: bool):
        self.is_game_over = status
