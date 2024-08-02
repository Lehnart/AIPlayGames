import random
from typing import List


class AIPlayer:

    def next_move(self, events: List):
        return random.choice([(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)])
