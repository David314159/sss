import pygame

pressed_keys = pygame.key.get_pressed()


def detect_keys(*keys):
    output = set()
    for k in keys:
        if pressed_keys[k]:
            output.add(k)
    return output


def detect_wasd():
    return detect_keys(pygame.K_a, pygame.K_w, pygame.K_s, pygame.K_d)
