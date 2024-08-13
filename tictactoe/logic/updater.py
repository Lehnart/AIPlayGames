import pickle
from typing import List

from tictactoe.player.q_ai_player import QAIPlayer
from tictactoe.player.q_learning_ai_player import QLearningAIPlayer
from tictactoe.logic.state import State, GameStatus


class Updater:

    def __init__(self, state: State):
        self.game_count = 0
        self.state = state
        self.player1 = QAIPlayer(0,"tictactoe/res/q.bin")
        self.player2 = QLearningAIPlayer(1)

    def update(self, events: List):
        next_move = self.get_next_move(events)
        if next_move is not None:
            self.play(*next_move)

        #print(self.state.board.to_string())
        if self.state.is_game_round_over():
            if self.state.game_status == GameStatus.DRAW:
                print("Draw")
            if self.state.game_status == GameStatus.WON:
                if self.state.winner == 0:
                    print("Player 1 won")
                elif self.state.winner == 1:
                    print("Player 2 won")
            self.end_game_round()

        if self.game_count > 50000:
            with open("q.bin", "bw") as q_file:
                pickle.dump(self.player1.Q, q_file)
            return False
        return True

    def get_next_move(self, events):
        if self.state.next_player == 0:
            return self.player1.next_move(self.state, events)
        elif self.state.next_player == 1:
            return self.player2.next_move(self.state, events)
        return None

    def play(self, row: int, col: int):
        if self.state.game_status is not GameStatus.PLAYING:
            return
        if not self.state.is_move_allowed(row, col):
            return
        self.state.play(row, col)

    def end_game_round(self):
        self.player1.end(self.state)
        self.player2.end(self.state)
        self.game_count += 1
        self.state.reset()
