import random
from typing import List

from tictactoe.player import Player
from tictactoe.logic.state import State
from tictactoe.player.abstract_player import AbstractPlayer


class RandomAIPlayer(AbstractPlayer):

    def next_move(self, state: State, events: List):
        return random.choice(state.board.get_empty_cases())

    def end(self, state: State):
        pass
