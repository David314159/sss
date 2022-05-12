from enum import Enum, auto
from typing import Callable, Any



class GameActionType(Enum):
    MOVE = auto()
    INTERACT = auto()
    ABILITY = auto()
    ATTACK = auto()
    CANCEL = auto()
    PASS = auto()
    OTHER = auto()


class GameAction:
    def __init__(self, action_type: GameActionType, ticks_remaining: int,
                 function_to_call: Callable[[], Any]):
        self.action_type = action_type
        self.ticks_remaining = ticks_remaining
        self.function_to_call = function_to_call

    def tick(self):
        self.ticks_remaining -= 1
        if self.ticks_remaining == 0:
            self.function_to_call()

    def is_finished(self):
        return self.ticks_remaining == 0


