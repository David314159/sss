from pygame import time
class Clock:
    def __init__(self):
        # the "ticks" in get_ticks are just milliseconds and have nothing to do with our game's ticks
        self.time = time.get_ticks()
        self.time_since_last_tick = time.get_ticks() - self.time

    def tick(self):
        self.time_since_last_tick = time.get_ticks() - self.time
        self.time = self.time_since_last_tick + self.time


clock = Clock()
