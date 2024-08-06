import pygame

from tictactoe.drawer import Drawer
from tictactoe.logic import Logic
from tictactoe.state import State


class Game:

    def __init__(self):
        self.state = State()
        self.drawer = Drawer(self.state)
        self.logic = Logic(self.state)

    def draw(self, surface: pygame.Surface):
        self.drawer.draw(surface)

    def update(self, events):
        return self.logic.update(events)
