import pygame

from tictactoe.graphics.drawer import Drawer
from tictactoe.logic.updater import Updater
from tictactoe.logic.state import State


class Game:

    def __init__(self):
        self.state = State()
        self.drawer = Drawer(self.state)
        self.updater = Updater(self.state)

    def draw(self, surface: pygame.Surface):
        self.drawer.draw(surface)

    def update(self, events):
        return self.updater.update(events)
