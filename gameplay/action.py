from enum import Enum, auto
from typing import Callable, Any
from gameplay.clock import clock

class GameActionType(Enum):

    # types of in game actions
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

        self.action_type = action_type # type of action
        self.function_to_call = function_to_call # function to call when action resolves
        self.start_time = clock.time # when the action began
        self.resolve_time = resolve_time # how long the action takes to resolve (milliseconds)
        self.finished = False # if the action is finished

    def tick(self):
        # if enough time has passed, the action resolves

        if clock.time - self.start_time >= self.resolve_time and not self.finished:
            self.function_to_call()
            self.finished = True



