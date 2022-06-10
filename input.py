import pygame


class Input:
    """Helper functions for detecting keyboard and mouse input."""
    def __init__(self):
        self.keys_pressed = pygame.key.get_pressed()
        self.mouse_buttons_pressed = pygame.mouse.get_pressed()

    def detect_keys(self, *keys):
        """
        Returns a set of ints corresponding to the keys that were detected as pressed.
        Only listens for keys specified in the "keys" argument.
        :param keys: The keypresses to detect.
        """
        output = set()
        for k in keys:
            if self.keys_pressed[k]:
                output.add(k)
        return output

    def detect_mouse_buttons(self):
        return self.mouse_buttons_pressed

    def detect_wasd(self):
        """Returns a set of ints corresponding to which of the WASD keys are currently pressed."""
        return self.detect_keys(pygame.K_a, pygame.K_w, pygame.K_s, pygame.K_d)

    def detect_qe(self):
        return self.detect_keys(pygame.K_q, pygame.K_e)

    def tick(self):
        self.keys_pressed = pygame.key.get_pressed()
        self.mouse_buttons_pressed = pygame.mouse.get_pressed()

input = Input()
