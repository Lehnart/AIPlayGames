import random


class Player:

    def __init__(self):
        pass

    def roll_dice(self):
        return [random.randint(1, 6) for _ in range(4)]

    def choose_combination(self, allowed_combinations):
        return random.choice(allowed_combinations)

    def does_turn_continue(self):
        return random.random() < 0.5
