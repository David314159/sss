from pygame import time


class Clock:
    def __init__(self):
        # the "ticks" in get_ticks are just milliseconds and have nothing to do with our game's ticks
        self.time = time.get_ticks()

    def tick(self):
        self.time = time.get_ticks()


clock = Clock()
