import pickle
from typing import List

from tictactoe.minimax_ai_player import MinimaxAIPlayer
from tictactoe.q_learning_ai_player import QLearningAIPlayer
from tictactoe.state import State, GameStatus


class Logic:

    def __init__(self, state: State):
        self.game_count = 0
        self.state = state
        self.player1 = MinimaxAIPlayer(0)
        self.player2 = MinimaxAIPlayer(1)

    def update(self, events: List):
        next_move = self.get_next_move(events)
        if next_move is not None:
            self.play(*next_move)

        print(self.state.board.to_string())
        if self.state.is_game_round_over():
            if self.state.game_status == GameStatus.DRAW:
                print("Draw")
            if self.state.game_status == GameStatus.WON:
                if self.state.winner == 0:
                    print("Player 1 won")
                elif self.state.winner == 1:
                    print("Player 2 won")
            self.end_game_round()

        if self.game_count > 20000:
            with open("q.bin", "bw") as q_file:
                pickle.dump(self.player2.Q, q_file)
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
        # if self.state.game_status.WON:
        #     reward = 1 if self.state.get_winner_index() == 1 else -1
        #     self.player2.update_q_table(self.state, reward)
        # elif self.state.game_status.DRAW:
        #     self.player2.update_q_table(self.state, 0)
        # self.player2.exploration_rate *= 0.999
        self.game_count += 1
        self.state.reset()
