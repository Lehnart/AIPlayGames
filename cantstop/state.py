import logging

logger = logging.getLogger(__name__)

class State:

    def __init__(self):
        self.player_heights = {k: 0 for k in range(2, 13)}
        self.max_heights = {2: 3, 3: 5, 4: 7, 5: 9, 6: 11, 7: 13, 8: 11, 9: 9, 10: 7, 11: 5, 12: 3}
        self.temporary_heights = {}

    def columns(self):
        return [k for k in self.max_heights]

    def claimed_columns(self):
        return [k for k in self.max_heights if self.player_heights[k] >= self.max_heights[k]]

    def is_game_over(self):
        won_columns = 0
        for col in self.columns():
            if self.player_heights[col] >= self.max_heights[col]:
                won_columns += 1
        return won_columns >= 3

    def find_allowed_combinations(self, dices):
        combinations = ((dices[0] + dices[1], dices[2] + dices[3]), (dices[0] + dices[2], dices[1] + dices[3]), (dices[0] + dices[3], dices[1] + dices[2]))
        allowed_combinations = []
        for combination in combinations:
            if self.is_combination_valid(combination):
                allowed_combinations.append(combination)
            else:
                if self.is_combination_valid([combination[0]]):
                    allowed_combinations.append([combination[0]])
                if self.is_combination_valid([combination[1]]):
                    allowed_combinations.append([combination[1]])

        return allowed_combinations

    def is_combination_valid(self, cols):
        next_temporary_heights = dict(self.temporary_heights)
        self.update_temporary_heights(cols, next_temporary_heights)
        if len(next_temporary_heights) > 3:
            return False
        for col in next_temporary_heights:
            if next_temporary_heights[col] > self.max_heights[col]:
                return False
        for col in next_temporary_heights:
            if col in self.claimed_columns():
                return False
        return True

    def update_temporary_heights(self, cols, temporary_heights):
        for col in cols:
            if col in temporary_heights:
                temporary_heights[col] = temporary_heights[col] + 1
            else:
                temporary_heights[col] = self.player_heights[col] + 1

    def update(self, cols):
        self.update_temporary_heights(cols, self.temporary_heights)

    def end_turn_with_fail(self):
        self.temporary_heights = {}

    def end_turn_with_success(self):
        for col in self.temporary_heights:
            self.player_heights[col] = self.temporary_heights[col]
        logger.info(f"player heights {self.player_heights}")
        self.temporary_heights = {}
