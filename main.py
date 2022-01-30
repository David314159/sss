from enum import Enum, auto

from action import Action, MOVE_ACTION, INTERACT_ACTION, ABILITY_ACTION, ATTACK_ACTION, PASS_ACTION
from directions import Direction
from player import Player


class OOGAction(Enum):
    QUIT = auto()


def print_menu(player: Player):
    print(f"""
        It's your turn.
        You are at ({player.x_square}, {player.y_square}).
        You have {player.action_points} action points.
        What do you do?
        1. Move
        2. Interact
        3. Use ability
        4. Attack
        5. Pass
        6. Exit
        """)


def get_player_action(player: Player) -> Action | OOGAction:
    action_int = int(input())

    match action_int:
        case 1:
            return MOVE_ACTION
        case 2:
            return INTERACT_ACTION
        case 3:
            return ABILITY_ACTION
        case 4:
            return ATTACK_ACTION
        case 5:
            return PASS_ACTION
        case 6:
            return OOGAction.QUIT
        case _:
            print("Invalid option")
            get_player_action(player)


def do_player_action(player: Player, action: Action):
    player.action_points -= action.cost
    if player.action_points < 0:
        raise ValueError("Negative action points")
    match action.action_type:
        case MOVE_ACTION.action_type:
            direction = Direction.abbreviation_to_enum(
                input("Which direction do you want to move? ")
            )
            while direction == Direction.INVALID:
                print("Invalid direction")
                direction = Direction.abbreviation_to_enum(
                    input("Which direction do you want to move? ")
                )
            player.move_squares(direction, 1)


player = Player(0, 0, 0, 0, "Player")

while True:
    print_menu(player)
    action = get_player_action(player)
    if action == OOGAction.QUIT:
        break
    while player.action_points < action.cost:
        print("You do not have enough action points. Take a different action or pass.")
        print_menu(player)
        action = get_player_action(player)
    do_player_action(player, action)
