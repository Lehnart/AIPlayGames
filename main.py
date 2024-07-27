import pygame


def main():
    window = pygame.display.set_mode((640, 480))

    does_game_continue = True

    while does_game_continue:
        does_game_continue = update()
        draw(window)


def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def draw(surface: pygame.Surface):
    surface.fill(pygame.Color("black"))
    pygame.display.flip()


if __name__ == "__main__":
    main()
