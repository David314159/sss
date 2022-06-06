from enum import Enum, auto
from typing import Callable, Any
from gameplay.clock import clock

class GameActionType(Enum):
    MOVE = auto()
    INTERACT = auto()
    ABILITY = auto()
    ATTACK = auto()
    CANCEL = auto()
    PASS = auto()
    OTHER = auto()


class GameAction:
    def __init__(self, action_type: GameActionType, resolve_time: int,
                 function_to_call: Callable[[], Any]):
        # resolve_time is in milliseconds
        self.action_type = action_type
        self.function_to_call = function_to_call
        self.start_time = clock.time
        self.resolve_time = resolve_time
        self.finished = False

    def tick(self):
        if clock.time - self.start_time >= self.resolve_time and not self.finished:
            self.function_to_call()
            self.finished = True



