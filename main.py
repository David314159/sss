from enum import Enum, auto

from gameplay.action import GameAction, GameActionType
from entities.npc import NPC
from positions.directions import Direction
from entities.player import Player


class ProgramActionType(Enum):
    QUIT = auto()


def print_menu(player: Player):
    print(f"""
        It's your turn.
        You are at ({player.x_square}, {player.y_square}).
        What do you do?
        1. Move
        2. Interact
        3. Use ability
        4. Attack
        5. Pass
        6. Exit
        """)


def get_player_action_type(player: Player) -> GameActionType | ProgramActionType:
    action_int = int(input())

    match action_int:
        case 1:
            return GameActionType.MOVE
        case 2:
            return GameActionType.INTERACT
        case 3:
            return GameActionType.ABILITY
        case 4:
            return GameActionType.ATTACK
        case 5:
            return GameActionType.PASS
        case 6:
            return ProgramActionType.QUIT
        case _:
            print("Invalid option")
            get_player_action_type(player)


def get_player_action(action_type: GameActionType):
    match action_type:
        case GameActionType.MOVE:
            get_move_action()
        case GameActionType.INTERACT:
            get_interact_action()
        case GameActionType.ABILITY:
            get_ability_action()
        case GameActionType.ATTACK:
            get_attack_action()


def get_move_action():
    direction: Direction = Direction.abbreviation_to_enum(
        input("Which direction do you want to move? ")
    )
    while direction == Direction.INVALID:
        print("Invalid direction")
        direction = Direction.abbreviation_to_enum(
            input("Which direction do you want to move? ")
        )
    num_squares: int = int(input("How many squares do you want to move?"))


def take_turn(player: Player):
    print_menu(player)
    action = get_player_action(player)
    if action == ProgramActionType.QUIT:
        exit(0)
    do_player_action(player, action)
    print_menu(player)
    action = get_player_action(player)


def run_game():
    player: Player = Player(0, 0, 0, 0, "Player")
    npc: NPC = NPC(1, 0, 0, 0, "NPC")
    while True:
        print(f"")
        take_turn(player)


run_game()
