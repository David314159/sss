import pygame


class Input:
    def __init__(self):
        self.keys_pressed = pygame.key.get_pressed()

    def update_keys_pressed(self):
        self.keys_pressed = pygame.key.get_pressed()

    def detect_keys(self, *keys):
        output = set()
        for k in keys:
            if self.keys_pressed[k]:
                output.add(k)
        return output

    def detect_wasd(self):
        return self.detect_keys(pygame.K_a, pygame.K_w, pygame.K_s, pygame.K_d)

input = Input()

