import pygame

from graphics.sprite import entity_sprites
from graphics.window import screen, background_color


def tick_graphics():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    entity_sprites.update()
    entity_sprites.draw(screen)
    pygame.display.update()
    screen.fill(background_color)

