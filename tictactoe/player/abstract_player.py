import abc
from typing import List

from tictactoe.logic.state import State


class AbstractPlayer(abc.ABC):

    @abc.abstractmethod
    def next_move(self, state: State, events: List):
        pass

    @abc.abstractmethod
    def end(self, state: State):
        pass
