from enum import Enum, auto

from gameplay.action import GameAction, GameActionType
from entities.npc import NPC
from gameplay.game import Game
from positions.directions import Direction
from entities.player import Player
from positions.map import Map

global_map = Map(10, 10)
game = Game(set(), global_map.get_val(0, 0), global_map)

class ProgramActionType(Enum):
    QUIT = auto()




def run_game():
    player: Player = Player(0, 0, 0, 0, "Player")
    game.entities.add(player)
    while True:
        game.tick()
        print(f"")



run_game()
