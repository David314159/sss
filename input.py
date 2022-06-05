import pygame


class Input:
    def __init__(self):
        self.pressed_keys = pygame.key.get_pressed()

    def update_pressed_keys(self):
        self.pressed_keys = pygame.key.get_pressed()
        print(self.pressed_keys[pygame.K_w])

    def detect_keys(self, *keys):
        output = set()
        for k in keys:
            if self.pressed_keys[k]:
                output.add(k)
        return output

    def detect_wasd(self):
        return self.detect_keys(pygame.K_a, pygame.K_w, pygame.K_s, pygame.K_d)

input = Input()

