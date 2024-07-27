from pygame import Surface

from tictactoe.drawer import Drawer
from tictactoe.state import State


class Game:

    def __init__(self):
        self.state = State()
        self.drawer = Drawer(self.state)
