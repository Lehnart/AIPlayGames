import logging

from cantstop.player import Player
from cantstop.state import State

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def main():
    state = State()
    player = Player()
    while not state.is_game_over():
        dices = player.roll_dice()
        logger.info(f"Dices {dices}")
        allowed_combinations = state.find_allowed_combinations(dices)
        logger.info(f"Allowed combinations {allowed_combinations}")
        if allowed_combinations:
            combination = player.choose_combination(allowed_combinations)
            logger.info(f"Combination used {combination}")
            state.update(combination)

        if not allowed_combinations:
            logger.info(f"Failed to progress")
            state.end_turn_with_fail()

        elif not player.does_turn_continue():
            logger.info(f"Progressing")
            state.end_turn_with_success()

    print("over")


if __name__ == "__main__":
    main()
