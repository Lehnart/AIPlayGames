import random
from typing import List

from tictactoe.state import State, GameStatus


class MinimaxAIPlayer:
    def __init__(self, player):
        self.player = player

    def next_move(self, state: State, events: List):
        next_actions = []
        best_value = -10
        possible_actions = state.board.get_empty_cases()
        for possible_action in possible_actions:
            new_state = State.clone(state)
            new_state.play(*possible_action)
            value = self.minimax(new_state, 1, False)
            if value > best_value:
                next_actions = [possible_action]
                best_value = value
            if value == best_value:
                next_actions.append(possible_action)
                best_value = value
        return random.choice(next_actions)

    def minimax(self, state: State, depth: int, is_maximizing_player: bool):
        if state.game_status != GameStatus.PLAYING:
            if state.game_status == GameStatus.DRAW:
                return 0
            if state.winner == 0:
                if self.player == 0:
                    return 1
                return -1
            if state.winner == 1:
                if self.player == 1:
                    return 1
                return -1

        if is_maximizing_player:
            best_value = -10
            possible_actions = state.board.get_empty_cases()
            for possible_action in possible_actions:
                new_state = State.clone(state)
                new_state.play(*possible_action)
                value = self.minimax(new_state, depth + 1, False)
                best_value = max(best_value, value)
            return best_value

        else:
            best_value = +10
            possible_actions = state.board.get_empty_cases()
            for possible_action in possible_actions:
                new_state = State.clone(state)
                new_state.play(*possible_action)
                value = self.minimax(new_state, depth + 1, True)
                best_value = min(best_value, value)
            return best_value
