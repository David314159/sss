import sys
from enum import Enum, auto

from gameplay.action import GameAction, GameActionType
from entities.npc import NPC
from gameplay.game import Game, game
from positions.directions import Direction
from entities.player import Player
from positions.map import Map

import pygame
import time


class ProgramActionType(Enum):
    QUIT = auto()

def quit_game():
    pygame.quit()
    time.sleep(0.5)
    sys.exit(0)

def run_game():
    pygame.init()
    pygame.display.set_mode([1000, 1000])
    time.sleep(5)
    pygame.quit()
    player: Player = Player(0, 0, 0, 0, "Player")
    npc: NPC = NPC(0, 0, 0, 0, "enn pee cee")
    game.entities.add(player)
    game.entities.add(npc)
    game.ping_everything()
    while True:
        game.tick()
        print(f"")

run_game()
#comment for test commit