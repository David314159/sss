from enum import auto, Enum
from typing import Callable, Any

from entities.entity import Entity
from gameplay.action import GameAction, GameActionType, do_nothing
from gameplay.game import game
from gameplay.signal import Signal


class Ability:
    def __init__(self, name: str, ability_type: GameActionType, resolve_time: int,
                 function_to_call: Callable[["Entity"], Any],
                 energy_cost: int = 0, mana_cost: int = 0, health_cost: int = 0
                 ):
        self.name = name

        self.action_type = ability_type
        self.resolve_time = resolve_time
        self.function_to_call = function_to_call

        self.energy_cost = energy_cost
        self.mana_cost = mana_cost
        self.health_cost = health_cost

    def as_action(self, player: "Player"):
        def apply_cost():
            player.spend_energy(self.energy_cost)
            player.spend_mana(self.mana_cost)
            player.spend_health(self.health_cost)

        if player.current_energy - self.energy_cost >= 0 \
                and player.current_mana - self.mana_cost >= 0 \
                and player.current_health - self.health_cost > 0:
            return GameAction(self.name, self.action_type, self.resolve_time, apply_cost, lambda: self.function_to_call(player))
        else:
            return player.current_action


empty_slot = Ability("empty slot", GameActionType.OTHER, 0, lambda entity: None)


def punch_resolve(puncher: Entity):
    game.send_signal(Signal(sender=puncher, damage=puncher.strength, damage_type="normal"),
                     should_send_to=lambda entity:
                         entity is not puncher
                         and abs(puncher.x_pos - entity.x_pos) < 100
                         and abs(puncher.y_pos - entity.x_pos) < 100
                     )


punch = Ability("punch", GameActionType.ATTACK, 250, punch_resolve,
                energy_cost=50, mana_cost=10)
