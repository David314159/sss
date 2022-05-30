import pygame
from pygame import key

pressed_keys = key.get_pressed()


def detect_wasd():
    if pressed_keys[pygame.K_w]:
        pass
    if pressed_keys[pygame.K_a]:
        pass
    if pressed_keys[pygame.K_s]:
        pass
    if pressed_keys[pygame.K_d]:
        pass
