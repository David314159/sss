from typing import Callable, Any

from gameplay.clock import clock
from positions.directions import Direction
from gameplay.signal import Signal
from pygame import time

class ContCalledFunc:
    def __init__(self, name: str, func: Callable[[], Any], call_every: int, stop_after: int = None):
        self.name = name
        self.func = func
        self.call_every = call_every
        self.stop_after = stop_after
        self.start_time = clock.time
        self.effect_timer = 0

    def tick(self):
        self.effect_timer += clock.time_since_last_tick
        if self.effect_timer > self.call_every:
            self.func()
            self.effect_timer -= self.call_every

    def is_finished(self):
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
        self.speed = 5

        # Enable movement
        self.to_call_continuously.add(ContCalledFunc("movement", self.move, 50))

    def call_continuously(self, func_name: str, func: Callable[[], Any], call_every: int, stop_after: int = None):
        self.to_call_continuously.add(ContCalledFunc(func_name, func, call_every, stop_after))

    def stop_calling(self, name: str):
        func_specs_to_remove = set()
        for func_spec in self.to_call_continuously:
            if func_spec.name == name:
                func_specs_to_remove.add(func_spec)
        for func_spec in func_specs_to_remove:
            self.to_call_continuously.remove(func_spec)

    def handle_signal(self, signal: Signal):
        print("I am handling signal", signal)

    def set_x_velocity(self, x):
        self.x_velocity = x

    def set_y_velocity(self, x):
        self.x_velocity = x

    def set_velocity(self, x, y):
        self.x_velocity = x
        self.y_velocity = y

    def move(self):
        self.x_pos += self.x_velocity
        self.y_pos +=  self.y_velocity

    def tick(self):
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
