from typing import List

import pygame

from tictactoe.player import Player
from tictactoe.logic.state import State


class HumanPlayer(Player):

    def end(self, state: State):
        pass

    def next_move(self, state: State, events: List):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_1:
                    return 2, 0
                if event.key == pygame.K_KP_2:
                    return 2, 1
                if event.key == pygame.K_KP_3:
                    return 2, 2
                if event.key == pygame.K_KP_4:
                    return 1, 0
                if event.key == pygame.K_KP_5:
                    return 1, 1
                if event.key == pygame.K_KP_6:
                    return 1, 2
                if event.key == pygame.K_KP_7:
                    return 0, 0
                if event.key == pygame.K_KP_8:
                    return 0, 1
                if event.key == pygame.K_KP_9:
                    return 0, 2
