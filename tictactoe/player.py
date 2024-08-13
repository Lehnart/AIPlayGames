import abc
from typing import List

from tictactoe.state import State


class Player(abc.ABC):

    @abc.abstractmethod
    def next_move(self, state: State, events: List):
        pass

    @abc.abstractmethod
    def end(self, state: State):
        pass
