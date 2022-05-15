from enum import Enum, auto

from gameplay.action import GameAction, GameActionType
from entities.npc import NPC
from gameplay.game import Game, game
from positions.directions import Direction
from entities.player import Player
from positions.map import Map


class ProgramActionType(Enum):
    QUIT = auto()


def run_game():
    player: Player = Player(0, 0, 0, 0, "Player")
    npc: NPC = NPC(0, 0, 0, 0, "enn pee cee")
    game.entities.add(player)
    game.entities.add(npc)
    game.ping_everything()
    while True:
        game.tick()
        print(f"")

run_game()
