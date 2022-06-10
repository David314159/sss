from pygame import time

class Clock:
    def __init__(self):
        # anything time dependent in the game will use this

        # the "ticks" in get_ticks are just milliseconds and have nothing to do with our game's ticks
        self.time = time.get_ticks() # time since python.__init__() was called (milliseconds)

        self.time_since_last_tick = 0 # time since the last game tick (milliseconds)

    def tick(self):
        # update the clock

        self.time_since_last_tick = time.get_ticks() - self.time
        self.time = time.get_ticks()


clock = Clock()
