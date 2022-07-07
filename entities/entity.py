from typing import Callable, Any

from gameplay.clock import clock
from gameplay.signal import Signal
from graphics.sprite import EntitySprite, EffectSprite
from physics.vector2d import Vector2D


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
        """If enough time has passed, calls the underlying function and lowers the timer.
        Repeats until no time remains."""

        self.effect_timer += clock.time_since_last_tick
        while self.effect_timer > 0:
            self.func()
            self.effect_timer -= self.call_every

    def is_finished(self):
        """Returns true if the function has been called for the desired amount of time"""

        return self.stop_after is not None and (clock.time - self.start_time) > self.stop_after


class Entity:
    """Represents everything in the game that has a location and can be targeted."""

    def __init__(self, name: str, position: Vector2D, sprite: EntitySprite, initial_velocity: Vector2D = None):
        self.name = name
        self.position = position
        self.sprite = sprite
        self.sprite.entity = self
        self.has_ticked = False
        self.to_call_continuously = set()

        if initial_velocity is None:
            self.velocity = Vector2D(0, 0)
        else:
            self.velocity = initial_velocity

        # Enable movement
        self.call_continuously("movement", self.move, 20)

    def call_continuously(self, func_name: str, func: Callable[[], Any], call_every: int, stop_after: int = None):
        """Adds a new continously called function to this entity.
        Can be used for over-time effects, movement, or anything else that repeats on a timer"""

        self.to_call_continuously.add(ContCalledFunc(func_name, func, call_every, stop_after))

    def stop_calling(self, name: str):
        """given the name of a function, stop calling that function early"""

        func_specs_to_remove = set()
        for func_spec in self.to_call_continuously:
            if func_spec.name == name:
                func_specs_to_remove.add(func_spec)
        for func_spec in func_specs_to_remove:
            self.to_call_continuously.remove(func_spec)

    def handle_signal(self, signal: Signal):
        """handle a signal from another entity or the game"""
        pass

    def set_velocity(self, x, y):
        # sets overall velocity

        self.velocity.x = x
        self.velocity.y = y

    def should_die(self) -> bool:
        return False

    def on_death(self):
        """Should be called when this entity dies."""
        pass

    def die(self):
        self.on_death()
        self.sprite.remove_entity_sprite()

    def move(self):
        """Move based on own velocity.
        This should almost always be running as a continuous function."""
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

    def first_tick(self):
        pass

    def tick(self):
        """Tick this entity, handling its continuously called functions.
        Check for death, and call self.on_death() if dead.
        """

        if not self.has_ticked:
            self.first_tick()
            self.has_ticked = True

        func_specs_to_remove = set()
        for func_spec in self.to_call_continuously:
            func_spec.tick()
            if func_spec.is_finished():
                func_specs_to_remove.add(func_spec)

        for func_spec in func_specs_to_remove:
            self.to_call_continuously.remove(func_spec)

        if self.should_die():
            self.die()
