import pygame

from graphics.window import screen, background_color


def init_graphics():
    pygame.init()
    screen.fill(background_color)
