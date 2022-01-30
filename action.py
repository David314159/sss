from enum import Enum, auto


class ActionType(Enum):
    MOVE = auto()
    INTERACT = auto()
    ABILITY = auto()
    ATTACK = auto()
    PASS = auto()


class Action:
    def __init__(self, cost: int, action_type: ActionType):
        self.cost = cost
        self.action_type = action_type


MOVE_ACTION = Action(5, ActionType.MOVE)
INTERACT_ACTION = Action(2, ActionType.INTERACT)
ABILITY_ACTION = Action(5, ActionType.ABILITY)
ATTACK_ACTION = Action(3, ActionType.ATTACK)
PASS_ACTION = Action(0, ActionType.PASS)
