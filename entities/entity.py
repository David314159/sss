import math
from typing import Callable, Any

from gameplay.action import do_nothing, GameAction
from graphics.sprite import EntitySprite, ResourceBar

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
    def __init__(self, name: str, x_pos: int, y_pos: int, sprite: EntitySprite,
                 current_action = do_nothing,
                 max_health = 0, max_mana: int = 0, max_energy: int = 0,
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
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_velocity = 0
        self.y_velocity = 0

        # Resources
        self.max_health = max_health
        self.current_health =  max_health
        self.max_mana = max_mana
        self.current_mana = max_mana
        self.max_energy = max_energy
        self.current_energy = max_energy

        # Temporary states
        self.current_action = current_action

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
        self.magic_power  = magic_power

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
        if signal.damage > 0:
            self.current_health -= signal.damage

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
            print("dummie you are already doign that")
        else:
            print("not enough stuff")




    def move(self):
        # move based on own velocity
        # this should almost always be running as a continuous function
        self.x_pos += self.x_velocity
        self.y_pos += self.y_velocity

    def tick(self):
        # tick this entity, handling actions and continuous functions
        self.sprite.tick()
        self.health_bar.tick()
        self.mana_bar.tick()
        self.energy_bar.tick()

        if self.current_action.finished:
            self.current_action = do_nothing
        else:
            self.current_action.tick()

        func_specs_to_remove = set()
        for func_spec in self.to_call_continuously:
            func_spec.tick()
            if func_spec.is_finished():
                func_specs_to_remove.add(func_spec)

        for func_spec in func_specs_to_remove:
            self.to_call_continuously.remove(func_spec)
