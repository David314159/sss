import sys
from enum import Enum, auto

import graphics.window
from gameplay.action import do_nothing
from gameplay.game import *
from entities.npc import NPC
from entities.player import Player
from graphics.window import screen

import pygame
import time

from graphics.sprite import EntitySprite
from graphics.init import init_graphics
from graphics.tick import tick_graphics

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
    init_graphics()
    player: Player = Player(x_pos=5, y_pos=2,
                            current_action=do_nothing,
                            max_health=500, max_mana=500, max_energy=500,
                            speed=5, strength=50,
                            base_energy_regen=100, base_mana_regen=10, base_health_regen=5,
                            )
    npc: NPC = NPC("enn pee cee", x_pos=250, y_pos=250,
                   max_health=1000, max_mana=200, max_energy=500,
                   sprite=EntitySprite(img_path="goblin.jpeg", scale=(50, 50)))
    game.set_player(player)
    game.spawn_entity(player)
    game.spawn_entity(npc)
    game.ping_everything()

    while True:
        time.sleep(1 / TPS)
        tick_graphics()
        game.tick()


run_game()
