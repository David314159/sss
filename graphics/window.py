import pygame

import graphics
from graphics.sprite import sprites

screen = pygame.display.set_mode((800, 600))


def init_window():
    screen.fill((255, 0, 0))


def init_graphics():
    init_window()
    graphics.sprite.init_sprites()


def tick_graphics():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.fill((255, 0, 0))
    sprites.update()
    sprites.draw(screen)
    pygame.display.update()
