import sys
from enum import Enum, auto

import graphics.window
from gameplay.game import *
from entities.npc import NPC
from gameplay.action import GameAction, GameActionType
from entities.player import Player

import pygame
import time

class ProgramActionType(Enum):
    QUIT = auto()


def quit_game():
    pygame.quit()
    time.sleep(0.5)
    sys.exit(0)


def run_game():
    graphics.window.init_graphics()
    resolves_in_5_sec = GameAction(GameActionType.MOVE, 5000, lambda: print("resolved"))
    player: Player = Player(5, 2, current_action=resolves_in_5_sec)
    npc: NPC = NPC("enn pee cee", 0, 0)
    game = Game(set(), player)
    game.spawn_entity(player)
    game.spawn_entity(npc)
    game.ping_everything()
    pygame.init()

    while True:
        time.sleep(1)
        graphics.window.tick_graphics()
        game.tick()
        print("x:", player.x_pos)
        print("y:", player.y_pos)


run_game()
# comment for test commit
