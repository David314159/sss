import sys
from enum import Enum, auto

import graphics.window
from gameplay.game import *
from entities.npc import NPC
from entities.player import Player

import pygame
import time

TPS = 0.5

class ProgramActionType(Enum):
    QUIT = auto()


def quit_game():
    pygame.quit()
    time.sleep(0.5)
    sys.exit(0)


def run_game():
    graphics.window.init_graphics()
    player: Player = Player(5, 2, current_action=None)
    npc: NPC = NPC("enn pee cee", 0, 0)
    game = Game(set(), player)
    game.spawn_entity(player)
    game.spawn_entity(npc)
    game.ping_everything()
    pygame.init()

    while True:
        time.sleep(1 / TPS)
        graphics.window.tick_graphics()
        game.tick()
        print("x:", player.x_pos)
        print("y:", player.y_pos)


run_game()
# comment for test commit
