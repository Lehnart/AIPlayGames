from typing import List, Optional


class State:

    def __init__(self):
        self.next_player: int = 0
        self.grid: List[List[Optional[str]]] = [[None, None, None], [None, None, None], [None, None, None]]
        self.player_symbol = ["X", "O"]
