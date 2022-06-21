import math
from typing import Callable, Any

from entities.entity import Entity
from gameplay.action import nothing_action
from graphics.sprite import EntitySprite, ResourceBar, EffectSprite

from gameplay.clock import clock
from gameplay.signal import Signal

from physics.vector2d import Vector2D

class Being(Entity):
    """Represents everything in the game that has a location and can be targeted."""
    def __init__(self, name: str, position: Vector2D, sprite: EntitySprite,
                 current_action=nothing_action,
                 initial_velocity: Vector2D = None,
                 max_health: int = 0, max_mana: int = 0, max_energy: int = 0,
                 speed: int = 0, toughness: int = 0, dexterity: int = 0, strength: int = 0,
                 base_energy_regen: int = 0, base_mana_regen: int = 0, base_health_regen: int = 0,
                 life_power: int = 0, storm_power: int = 0, death_power: int = 0, fire_power: int = 0, nature_power: int = 0,
                 magic_power: int = 0):
        super().__init__(name, position, sprite, initial_velocity)

        # Lasting, constant attributes
        self.base_energy_regen = base_energy_regen
        self.base_mana_regen = base_mana_regen
        self.base_health_regen = base_health_regen

        # Resources
        self.max_health = max_health
        self.current_health = max_health
        self.max_mana = max_mana
        self.current_mana = max_mana
        self.max_energy = max_energy
        self.current_energy = max_energy

        # Temporary states
        self.current_action = current_action

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
        self.health_bar = ResourceBar(self, "current_health", max_health, proximity_rank=3, color=(255, 0, 0))
        self.mana_bar = ResourceBar(self, "current_mana", max_mana, proximity_rank=2, color=(0, 0, 255))
        self.energy_bar = ResourceBar(self, "current_energy", max_energy, proximity_rank=1, color=(255, 255, 0))

        self.call_continuously("base_regen_energy",
                               lambda: self.regen_energy(math.ceil(base_energy_regen/10)), 100)
        self.call_continuously("base_regen_mana",
                               lambda: self.regen_mana(math.ceil(base_mana_regen/10)), 100)
        self.call_continuously("base_regen_health",
                               lambda: self.regen_health(math.ceil(base_health_regen/10)), 100)

    def handle_signal(self, signal: Signal):
        """handle a signal from another entity or the game"""
        if signal.damage > 0:
            self.current_health -= signal.damage
        super().handle_signal(signal)

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
        super().on_death()
        death_effect = EffectSprite("death_effect.png", self.sprite.scale, 1000)
        death_effect.start_effect(self.position.x, self.position.y)

    def tick(self):
        """Tick this being, handling its actions and continuously called functions.
        Check for death, and call self.on_death() if dead.
        """
        if self.current_action.finished:
            self.current_action = nothing_action
        else:
            self.current_action.tick()

        super().tick()
