from enum import Enum, auto

from directions import Direction
from player import Player


class Action(Enum):
    MOVE = auto()
    INTERACT = auto()
    ABILITY = auto()
    ATTACK = auto()


class OOGAction(Enum):
    QUIT = auto()


def get_player_action() -> Action | OOGAction:
    action_int = int(input(
        """What do you do?
        1. Move
        2. Interact
        3. Use ability
        4. Attack
        5. Exit
        """
    ))

    match action_int:
        case 1:
            return Action.MOVE
        case 2:
            return Action.INTERACT
        case 3:
            return Action.ABILITY
        case 4:
            return Action.ATTACK
        case 5:
            return OOGAction.QUIT
        case _:
            print("Invalid option")
            get_player_action()


def do_player_action(player: Player):
    match action:
        case Action.MOVE:
            direction = Direction.abbreviation_to_enum(
                input("Which direction do you want to move? ")
            )
            while direction == Direction.INVALID:
                print("Invalid direction")
                direction = Direction.abbreviation_to_enum(
                    input("Which direction do you want to move? ")
                )
            player.move_squares(direction, 1)
            print(f"X:{player.x_square} Y:{player.y_square}")


player = Player(0, 0, 0, 0, "Player", 10)

while True:
    action = get_player_action()
    if action == OOGAction.QUIT:
        break
    do_player_action(player)
