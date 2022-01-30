from enum import Enum, auto


class GameActionType(Enum):
    MOVE = auto()
    INTERACT = auto()
    ABILITY = auto()
    ATTACK = auto()
    PASS = auto()


class GameAction:
    def __init__(self, action_type: GameActionType, cost: int):
        self.cost = cost
        self.action_type = action_type


MOVE_ACTION = GameAction(GameActionType.MOVE, 5)
INTERACT_ACTION = GameAction(GameActionType.INTERACT, 2)
ABILITY_ACTION = GameAction(GameActionType.ABILITY, 5)
ATTACK_ACTION = GameAction(GameActionType.ATTACK, 3)
PASS_ACTION = GameAction(GameActionType.PASS, 0)
