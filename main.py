import pygame

from tictactoe.game import Game


def main():
    window = pygame.display.set_mode((800, 800))
    tictactoe = Game()
    does_game_continue = True

    while does_game_continue:
        does_game_continue = update(tictactoe)
        draw(tictactoe, window)


def update(game: Game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def draw(game: Game, surface: pygame.Surface):
    surface.fill(pygame.Color("black"))
    game.drawer.draw(surface)
    pygame.display.flip()


if __name__ == "__main__":
    main()
