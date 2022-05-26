import pygame

screen = pygame.display.set_mode((800, 600))


def tick_graphics():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill((0, 0, 0))
    pygame.display.update()
