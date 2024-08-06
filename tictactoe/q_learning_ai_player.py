import random
from typing import List, Tuple, Dict

from tictactoe.state import State


class QLearningAIPlayer:

    def __init__(self):
        self.exploration_rate = 0.5
        self.Q = {}
        self.learning_rate = 0.1
        self.discount_factor = 0.9
        self.last_action = None
        self.last_state_string = None

    def next_move(self, state: State, events: List):

        self.update_q_table(state, 0)

        state_string = state.board.to_string()

        if random.uniform(0, 1) < self.exploration_rate or state_string not in self.Q:
            return self.explore(state, state_string)

        return self.exploit(state, state_string)

    def exploit(self, state, state_string):
        # Choose the action with the highest Q-value
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

    def explore(self, state, state_string):
        self.last_state_string = state_string
        self.last_action = random.choice(state.board.get_empty_cases())
        return self.last_action

    def update_q_table(self, next_state: State, reward):
        if self.last_action is None:
            return

        q_dict = dict(self.Q.get(self.last_state_string, {}))

        # Calculate the maximum Q-value for the next state
        next_q_dict: Dict[Tuple[int, int], float] = dict(self.Q.get(next_state.board.to_string(), {}))
        next_q_values = [next_q_dict[k] for k in next_q_dict.keys()]

        max_next_q_value = 0
        if len(next_q_values) > 0:
            max_next_q_value = max(next_q_values)

        if self.last_action not in q_dict:
            q_dict[self.last_action] = 0

        q_dict[self.last_action] += self.learning_rate * ((reward + self.discount_factor * max_next_q_value) - q_dict[self.last_action])

        self.Q[self.last_state_string] = q_dict
