from typing import List

import pygame

from tictactoe.state import State


class Logic:

    def __init__(self, state: State):
        self.state = state

    def update(self, events: List):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_1:
                    self.play(2, 0)
                if event.key == pygame.K_KP_2:
                    self.play(2, 1)
                if event.key == pygame.K_KP_3:
                    self.play(2, 2)
                if event.key == pygame.K_KP_4:
                    self.play(1, 0)
                if event.key == pygame.K_KP_5:
                    self.play(1, 1)
                if event.key == pygame.K_KP_6:
                    self.play(1, 2)
                if event.key == pygame.K_KP_7:
                    self.play(0, 0)
                if event.key == pygame.K_KP_8:
                    self.play(0, 1)
                if event.key == pygame.K_KP_9:
                    self.play(0, 2)

    def play(self, row: int, col: int):
        if self.check_if_game_is_over():
            return
        if not self.is_case_allowed(row, col):
            return
        self.state.set_symbol(row, col)

    def check_if_game_is_over(self):
        game_over_status = self.is_game_over()
        self.state.set_game_over_status(game_over_status)
        return game_over_status

    def is_case_allowed(self, row, col):
        return self.state.get_symbol_in_case(row, col) is None

    def is_game_over(self):
        lines = [
            [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]
        ]
        for line in lines:
            symbols = {}
            for row, col in line:
                symbol = self.state.get_symbol_in_case(row, col)
                if symbol is None:
                    continue
                if symbol not in symbols:
                    symbols[symbol] = 0
                symbols[symbol] += 1
            for symbol in symbols:
                if symbols[symbol] == 3:
                    return True

        return False
