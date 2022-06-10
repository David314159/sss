import pygame

import graphics
from graphics.sprite import sprites

screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Triple S')
background_color = (30, 50, 30)

def init_window():
    screen.fill(background_color)


def init_graphics():
    pygame.init()
    init_window()

def tick_graphics():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.fill(background_color)
    sprites.update()
    sprites.draw(screen)
    pygame.display.update()
