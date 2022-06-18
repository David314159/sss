from typing import Callable, Any

from gameplay.action import GameAction
from gameplay.game import game
from gameplay.signal import Signal


class Ability:
    """An info class used to generate an action (e.g. punch) and apply the cost of it to the player."""
    def __init__(self, name: str, resolve_time: int,
                 function_to_call: Callable[["Entity"], Any], can_move: bool = False,
                 energy_cost: int = 0, mana_cost: int = 0, health_cost: int = 0
                 ):
        self.name = name

        self.resolve_time = resolve_time
        self.function_to_call = function_to_call

        self.can_move = can_move
        self.energy_cost = energy_cost
        self.mana_cost = mana_cost
        self.health_cost = health_cost

    def as_action(self, player: "Player"):
        """Generates and returns the action."""
        return GameAction(self.name, self.resolve_time, self.can_move, lambda: None, lambda: self.function_to_call(player))


def punch_resolve(puncher: "Entity"):
    """The function to be called when a punch action resolves."""
    game.send_signal(Signal(sender=puncher, damage=puncher.strength, damage_type="normal"),
                     should_send_to=lambda entity:
                         entity is not puncher
                         and abs(puncher.x_pos - entity.x_pos) < 100
                         and abs(puncher.y_pos - entity.x_pos) < 100
                     )


empty_slot = Ability("empty slot", 0, lambda player: None)

punch = Ability("punch", 250, punch_resolve,
                energy_cost=50, mana_cost=10)
