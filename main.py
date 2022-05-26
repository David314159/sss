import sys
from enum import Enum, auto

import graphics.window
from entities.npc import NPC
from gameplay.game import Game, game
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
    player: Player = Player("Player")
    npc: NPC = NPC("enn pee cee")
    game.entities.add(player)
    game.entities.add(npc)
    game.ping_everything()
    while True:
        graphics.window.tick_graphics()
        game.tick()

run_game()
# comment for test commit
