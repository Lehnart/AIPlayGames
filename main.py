import pygame

from tictactoe.game import Game


def main():
    window = pygame.display.set_mode((800, 800))
    tictactoe = Game()
    does_game_continue = True

    while does_game_continue:
        #draw(tictactoe, window)
        does_game_continue = update(tictactoe)


def update(game: Game):
    events = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        events.append(event)

    does_game_continue = game.update(events)

    return does_game_continue


def draw(game: Game, surface: pygame.Surface):
    surface.fill(pygame.Color("black"))
    game.draw(surface)
    pygame.display.flip()


if __name__ == "__main__":
    main()
