from enum import auto, Enum
from typing import Callable, Any

from gameplay.action import GameAction, do_nothing
from gameplay.game import game
from gameplay.signal import Signal


class Ability:
    def __init__(self, name: str, resolve_time: int,
                 function_to_call: Callable[["Entity"], Any],
                 energy_cost: int = 0, mana_cost: int = 0, health_cost: int = 0
                 ):
        self.name = name

        self.resolve_time = resolve_time
        self.function_to_call = function_to_call

        self.energy_cost = energy_cost
        self.mana_cost = mana_cost
        self.health_cost = health_cost

    def as_action(self, player: "Player"):
        return GameAction(self.name, self.resolve_time, lambda: None, lambda: self.function_to_call(player))


def punch_resolve(puncher: "Entity"):
    game.send_signal(Signal(sender=puncher, damage=puncher.strength, damage_type="normal"),
                     should_send_to=lambda entity:
                         entity is not puncher
                         and abs(puncher.x_pos - entity.x_pos) < 100
                         and abs(puncher.y_pos - entity.x_pos) < 100
                     )


empty_slot = Ability("empty slot", 0, lambda player: None)

punch = Ability("punch", 250, punch_resolve,
                energy_cost=50, mana_cost=10)
