import pickle
import random
from typing import List

from tictactoe.player import Player
from tictactoe.logic.state import State


class QAIPlayer(Player):

    def __init__(self, player: int, q_file_str: str):
        with open(q_file_str, "br") as q_file:
            self.Q = pickle.load(q_file)
        self.last_action = None
        self.last_state_string = None
        self.player = player

    def next_move(self, state: State, events: List):
        state_string = state.board.to_string()
        q_values = self.Q[state_string]
        possible_actions = state.board.get_empty_cases()
        for row, col in possible_actions:
            if (row, col) not in q_values:
                q_values[(row, col)] = 0
        empty_q_values = [q_values[(row, col)] for row, col in possible_actions]
        max_q_value = max(empty_q_values)  # find the maximum Q-value among the empty cells Qvalue
        max_q_indices = [i for i in range(len(possible_actions)) if empty_q_values[i] == max_q_value]  # retrieves the indices of empty cells that have the maximum Q-value.
        max_q_index = random.choice(max_q_indices)  # if there are multiple cells with same maximum Q value select 1 randomly
        action = tuple(possible_actions[max_q_index])  # retrieves the indices of the selected empty cell based on max_q_index
        self.last_state_string = state_string
        self.last_action = action
        return action

    def end(self, state: State):
        pass
