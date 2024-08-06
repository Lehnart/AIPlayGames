import random
from time import time
from typing import List

from tictactoe.state import State


class RandomAIPlayer:

    def __init__(self):
        self.last_update = time()

    def next_move(self, state: State, events: List):
        if self.last_update is None:
            self.last_update = time()
            return None

        # dt = time() - self.last_update
        # if dt < 0.0001:
        #     return None

        self.last_update = None
        return random.choice(state.board.get_empty_cases())
