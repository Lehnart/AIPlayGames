import pygame

from tictactoe.state import State


class Drawer:

    def __init__(self, state: State):
        self.state = state
        self.board_image = pygame.image.load("tictactoe/res/board.png")
        self.x_marker = pygame.image.load("tictactoe/res/X.png")
        self.o_marker = pygame.image.load("tictactoe/res/O.png")
        self.symbol_to_marker_map = {"X": self.x_marker, "O": self.o_marker}

    def draw(self, surface: pygame.Surface):
        surface.blit(self.board_image, (0, 0))
        for row, col, symbol in self.state.board.get_cases_with_symbols():
            symbol_image = self.symbol_to_marker_map[symbol]
            x, y = self.col_to_x(col), self.row_to_y(row)
            surface.blit(symbol_image, (x, y))

    @staticmethod
    def row_to_y(row):
        return 10 + (265 * row)

    @staticmethod
    def col_to_x(col):
        return 10 + (265 * col)
