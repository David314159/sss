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
        self.start_time = time.get_ticks()
        self.effect_timer = 0


class Entity:
    def __init__(self, name: str, x_pos: int, y_pos: int, current_action = None):

        # Lasting, constant attributes
        self.name = name

        # Lasting, variable attributes
        self.x_pos = x_pos
        self.y_pos = y_pos

        # Temporary states
        self.current_action = current_action
        self.moving = False
        self.direction_moving = None

        # Effects over time
        self.to_call_continuously: set[ContCalledFunc] = set()

        # Stats
        self.speed = 5

    def call_continuously(self, func_name: str, func: Callable[[], Any], call_every: int, stop_after: int = None):
        self.to_call_continuously.add(ContCalledFunc(func_name, func, call_every, stop_after))

    def handle_signal(self, signal: Signal):
        print("I am handling signal", signal)

    def tick(self):
        if self.current_action is not None:
            if self.current_action.finished:
                self.current_action = None
            else:
                self.current_action.tick()

        for func_spec in self.to_call_continuously:
            if func_spec.effect_timer > func_spec.call_every:
                func_spec.func()
                func_spec.effect_timer -= func_spec.call_every
            if (clock.time - func_spec.start_time) > func_spec.stop_after:
                self.to_call_continuously.remove(func_spec)
