import math
from typing import Callable, Any

from gameplay.action import nothing_action
from graphics.sprite import EntitySprite, ResourceBar, EffectSprite

from gameplay.clock import clock
from gameplay.signal import Signal

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
    def __init__(self, name: str, position: Vector2D, sprite: EntitySprite,
                 current_action=nothing_action,
                 max_health: int = 0, max_mana: int = 0, max_energy: int = 0,
                 speed: int = 0, toughness: int = 0, dexterity: int = 0, strength: int = 0,
                 base_energy_regen: int = 0, base_mana_regen: int = 0, base_health_regen: int = 0,
                 life_power: int = 0, storm_power: int = 0, death_power: int = 0, fire_power: int = 0, nature_power: int = 0,
                 magic_power: int = 0):

        # Lasting, constant attributes
        self.name = name
        self.base_energy_regen = base_energy_regen
        self.base_mana_regen = base_mana_regen
        self.base_health_regen = base_health_regen

        # Lasting, variable attributes
        self.position = position
        self.velocity = Vector2D(0, 0)

        # Resources
        self.max_health = max_health
        self.current_health = max_health
        self.max_mana = max_mana
        self.current_mana = max_mana
        self.max_energy = max_energy
        self.current_energy = max_energy

        # Temporary states
        self.current_action = current_action
        self.alive = True

        # Effects over time
        self.to_call_continuously: set[ContCalledFunc] = set()

        # Physical stats
        self.speed = speed
        self.toughness = toughness
        self.dexterity = dexterity
        self.strength = strength

        # Mage stats
        self.life_power = life_power
        self.storm_power = storm_power
        self.death_power = death_power
        self.fire_power = fire_power
        self.nature_power = nature_power
        self.magic_power = magic_power

        # Graphics
        self.sprite = sprite
        self.sprite.entity = self
        self.health_bar = ResourceBar(self, "current_health", max_health, proximity_rank=3, color=(255, 0, 0))
        self.mana_bar = ResourceBar(self, "current_mana", max_mana, proximity_rank=2, color=(0, 0, 255))
        self.energy_bar = ResourceBar(self, "current_energy", max_energy, proximity_rank=1, color=(255, 255, 0))

        # Enable movement
        self.call_continuously("movement", self.move, 20)

        self.call_continuously("base_regen_energy",
                               lambda: self.regen_energy(math.ceil(base_energy_regen/10)), 100)
        self.call_continuously("base_regen_mana",
                               lambda: self.regen_mana(math.ceil(base_mana_regen/10)), 100)
        self.call_continuously("base_regen_health",
                               lambda: self.regen_health(math.ceil(base_health_regen/10)), 100)

    def call_continuously(self, func_name: str, func: Callable[[], Any], call_every: int, stop_after: int = None):
        """Adds a new continously called function to this entity.
        Can be used for over-time effects, movement, or anything else that repeats on a timer"""

        self.to_call_continuously.add(ContCalledFunc(func_name, func, call_every, stop_after))

    def stop_calling(self, name: str):
        """given the name, stop calling that function early"""

        func_specs_to_remove = set()
        for func_spec in self.to_call_continuously:
            if func_spec.name == name:
                func_specs_to_remove.add(func_spec)
        for func_spec in func_specs_to_remove:
            self.to_call_continuously.remove(func_spec)

    def handle_signal(self, signal: Signal):
        """handle a signal from another entity or the game"""
        if signal.damage > 0:
            self.current_health -= signal.damage

    def set_velocity(self, x, y):
        # sets overall velocity

        self.velocity.x = x
        self.velocity.y = y

    def regen_energy(self, amount: int):
        if self.current_energy + amount > self.max_energy:
            self.current_energy = self.max_energy
        else:
            self.current_energy += amount
    
    def spend_energy(self, amount: int):
        if self.current_energy - amount < 0:
            self.current_energy = 0
        else:
            self.current_energy -= amount

    def regen_mana(self, amount: int):
        if self.current_mana + amount > self.max_mana:
            self.current_mana = self.max_mana
        else:
            self.current_mana += amount

    def spend_mana(self, amount: int):
        if self.current_mana - amount < 0:
            self.current_mana = 0
        else:
            self.current_mana -= amount

    def regen_health(self, amount: int):
        if self.current_health + amount > self.max_health:
            self.current_health = self.max_health
        else:
            self.current_health += amount

    def spend_health(self, amount: int):
        if self.current_health - amount < 1:
            self.current_health = 1
        else:
            self.current_health -= amount

    def my_ability(self, ability: "Ability") -> "Ability":
        return ability

    def attempt_ability(self, ability: "Ability"):
        if self.current_energy - ability.energy_cost >= 0 \
                and self.current_mana - ability.mana_cost >= 0 \
                and self.current_health - ability.health_cost > 0 \
                and self.current_action.name != ability.name:
            self.spend_energy(ability.energy_cost)
            self.spend_mana(ability.mana_cost)
            self.spend_health(ability.health_cost)
            self.current_action = ability.as_action(self)
        elif self.current_action.name == ability.name:
            # TODO change from print statements
            print("dummie you are already doing that")
        else:
            print("not enough stuff")

    def is_alive(self) -> bool:
        return self.current_health > 0

    def on_death(self):
        """Should be called when this entity dies."""
        self.sprite.remove_entity_sprite()
        death_effect = EffectSprite("death_effect.png", self.sprite.scale, 1000)
        death_effect.start_effect(self.position.x, self.position.y)

    def move(self):
        """Move based on own velocity.
        This should almost always be running as a continuous function."""
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

    def tick(self):
        """Tick this entity, handling its actions and continuously called functions.
        Check for death, and call self.on_death() if dead.
        """

        if self.current_action.finished:
            self.current_action = nothing_action
        else:
            self.current_action.tick()

        func_specs_to_remove = set()
        for func_spec in self.to_call_continuously:
            func_spec.tick()
            if func_spec.is_finished():
                func_specs_to_remove.add(func_spec)

        for func_spec in func_specs_to_remove:
            self.to_call_continuously.remove(func_spec)

        if not self.is_alive():
            self.alive = False
            self.on_death()
