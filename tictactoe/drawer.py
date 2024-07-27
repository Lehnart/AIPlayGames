import pygame

from tictactoe.state import State


class Drawer:

    def __init__(self, state: State):
        self.board_image = pygame.image.load("tictactoe/res/board.png")
        self.x_marker = pygame.image.load("tictactoe/res/X.png")
        self.o_marker = pygame.image.load("tictactoe/res/O.png")

    def draw(self, surface: pygame.Surface):
        surface.blit(self.board_image, (0, 0))
        surface.blit(self.x_marker, (10, 10))
        surface.blit(self.o_marker, (540, 540))
