import pygame


class Input:
    """Helper functions for detecting keyboard and mouse input."""
    def __init__(self):
        self.keys_pressed = pygame.key.get_pressed()

    def update_keys_pressed(self):
        """Updates the list of keys pressed. Should be called once every tick."""
        self.keys_pressed = pygame.key.get_pressed()

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

    def detect_wasd(self):
        """Returns a set of ints corresponding to which of the WASD keys are currently pressed."""
        return self.detect_keys(pygame.K_a, pygame.K_w, pygame.K_s, pygame.K_d)


input = Input()
