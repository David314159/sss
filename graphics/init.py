import pygame

from graphics.window import screen, background_color


def init_graphics():
    """Initialize pygame and fill the screen"""
    pygame.init()
    screen.fill(background_color)
