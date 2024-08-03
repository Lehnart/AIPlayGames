from typing import List, Optional, Tuple


class Board:

    def __init__(self):
        self.row_count = 3
        self.col_count = 3
        self.grid: List[List[Optional[str]]] = self.init_grid()

    def init_grid(self):
        return [[None for _ in range(self.col_count)] for _ in range(self.row_count)]

    def to_string(self):
        string = ""
        for row in range(self.row_count):
            for col in range(self.col_count):
                symbol = self.get_symbol_in_case(row, col)
                if symbol is None:
                    string += " "
                else:
                    string += symbol
            string += '\n'
        return string

    def get_empty_cases(self) -> List[Tuple[int, int]]:
        symbols = []
        for i in range(self.row_count):
            for j in range(self.col_count):
                symbol = self.get_symbol_in_case(i, j)
                if symbol is None:
                    symbols.append((i, j))
        return symbols

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

    def set_symbol(self, row: int, col: int, symbol: str):
        self.grid[row][col] = symbol
