import sys
from enum import Enum, auto

import graphics.window
from gameplay.game import *
from entities.npc import NPC
from entities.player import Player

import pygame
import time

from graphics.sprite import SSSSprite

TPS = 20
"""Ticks per second. All tick() methods should be called at this rate."""


class ProgramActionType(Enum):
    """Represents a type of action that the player can take on the game itself, e.g. quitting."""
    QUIT = auto()


def quit_game():
    """Exits the program."""
    pygame.quit()
    time.sleep(0.5)
    sys.exit(0)


def run_game():
    """The main function. Starts the program."""
    graphics.window.init_graphics()
    player: Player = Player(x_pos=5, y_pos=2, current_action=None, speed=5, max_health=500, max_mana=500, strength=50)
    npc: NPC = NPC("enn pee cee", x_pos=250, y_pos=250,  max_health=1000, max_mana=200,
                   sprite=SSSSprite(img_path="goblin.jpeg", scale=(50, 50)))
    game.set_player(player)
    game.spawn_entity(player)
    game.spawn_entity(npc)
    game.ping_everything()

    while True:
        time.sleep(1 / TPS)
        graphics.window.tick_graphics()
        game.tick()


run_game()
