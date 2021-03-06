from typing import Callable, Any

from gameplay.clock import clock

class GameAction:
    """Used to represent an action that an entity takes. Handles the actual execution of the action."""
    def __init__(self, name: str, resolve_time: int, can_move, function_to_call_first: Callable[[], Any],
                 function_to_call_last: Callable[[], Any]):
        self.name = name
        self.can_move = can_move
        self.start_time = clock.time # when the action began
        self.resolve_time = resolve_time # how long the action takes to resolve (milliseconds)
        self.finished = False # if the action is finished
        self._has_ticked = False

        self.function_to_call_first = function_to_call_first
        self.function_to_call_last = function_to_call_last

    def tick(self):
        if not self._has_ticked:
            self.function_to_call_first()
            self._has_ticked = True

        # if enough time has passed, the action resolves
        if clock.time - self.start_time >= self.resolve_time and not self.finished:
            self.function_to_call_last()
            self.finished = True

nothing_action = GameAction("do nothing", 0, True, lambda: None, lambda: None)