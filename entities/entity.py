from typing import Callable, Any

from gameplay.clock import clock
from gameplay.signal import Signal

class ContCalledFunc:
    """Object for calling functions continuously"""

    def __init__(self, name: str, func: Callable[[], Any], call_every: int, stop_after: int = None):
        self.name = name # string so that the continuous function can be identified
        self.func = func # the function itself
        self.call_every = call_every # how often to call (milliseconds)
        self.stop_after = stop_after # when to stop  (milliseconds)
        self.start_time = clock.time # when it was started (milliseconds)
        self.effect_timer = 0 # temporary for keeping track of calls, updates each tick

    def tick(self):
        # ticks the continuously called function

        self.effect_timer += clock.time_since_last_tick
        while self.effect_timer > 0:
            self.func()
            self.effect_timer -= self.call_every

        # if enough time has passed, call the function and lower the timer
        # continue until no time remains

    def is_finished(self):
        # returns true if the function has been called for the desired amount of time

        return self.stop_after is not None and (clock.time - self.start_time) > self.stop_after


class Entity:
    def __init__(self, name: str, x_pos: int, y_pos: int, current_action = None):

        # Lasting, constant attributes
        self.name = name

        # Lasting, variable attributes
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_velocity = 0
        self.y_velocity = 0

        # Temporary states
        self.current_action = current_action
        self.direction_moving = None

        # Effects over time
        self.to_call_continuously: set[ContCalledFunc] = set()

        # Stats
        self.speed = 3

        # Enable movement
        self.to_call_continuously.add(ContCalledFunc("movement", self.move, 20))

    def call_continuously(self, func_name: str, func: Callable[[], Any], call_every: int, stop_after: int = None):
        # Adds a new continously called function to this entity
        # can be used for over-time effects, movement, or anything else that repeats on a timer

        self.to_call_continuously.add(ContCalledFunc(func_name, func, call_every, stop_after))

    def stop_calling(self, name: str):
        # given the name, stop calling the function early

        func_specs_to_remove = set()
        for func_spec in self.to_call_continuously:
            if func_spec.name == name:
                func_specs_to_remove.add(func_spec)
        for func_spec in func_specs_to_remove:
            self.to_call_continuously.remove(func_spec)

    def handle_signal(self, signal: Signal):
        # handle a signal from another entity or the game

        print("I am handling signal", signal)

    def set_x_velocity(self, x):
        # sets the x velocity

        self.x_velocity = x

    def set_y_velocity(self, x):
        # sets the y velocity

        self.x_velocity = x

    def set_velocity(self, x, y):
        # sets overall velocity

        self.x_velocity = x
        self.y_velocity = y

    def move(self):
        # move based on own velocity
        # this should almost always be running as a continuous function
        self.x_pos += self.x_velocity
        self.y_pos += self.y_velocity

    def tick(self):
        # tick this entity, handling actions and continuous functions
        if self.current_action is not None:
            if self.current_action.finished:
                self.current_action = None
            else:
                self.current_action.tick()

        func_specs_to_remove = set()
        for func_spec in self.to_call_continuously:
            func_spec.tick()
            if func_spec.is_finished():
                func_specs_to_remove.add(func_spec)

        for func_spec in func_specs_to_remove:
            self.to_call_continuously.remove(func_spec)
