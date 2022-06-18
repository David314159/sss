from pygame import time

class Clock:
    """The game's clock. Anything time-dependent in the game will use this. There should only be one instance."""
    def __init__(self):
        # the "ticks" in get_ticks are just milliseconds and have nothing to do with our game's ticks
        # get_ticks returns the time in milliseconds since python.__init__() was called
        self.time = time.get_ticks()

        # Time since the last game tick (milliseconds)
        # Set to 0 initially so that anything relying on it will basically do nothing until clock.tick() is first called
        # (because it will think no time has passed)
        self.time_since_last_tick = 0

    def tick(self):
        """Update the clock."""

        self.time_since_last_tick = time.get_ticks() - self.time
        self.time = time.get_ticks()


clock = Clock()
