import sys
from enum import Enum, auto

from gameplay.action import nothing_action
from gameplay.game import *
from entities.npc import NPC
from entities.player import Player

import pygame
import time

from graphics.sprite import EntitySprite
from graphics.init import init_graphics
from graphics.tick import tick_graphics
from physics.vector2d import Vector2D

TPS = 60
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
    player: Player = Player(position=Vector2D(50, 100),
                            current_action=nothing_action,
                            max_health=500, max_mana=500, max_energy=500,
                            speed=5,
                            base_energy_regen=100, base_mana_regen=10, base_health_regen=5,
                            )
    npc: NPC = NPC("enn pee cee", position=Vector2D(250, 250), speed=5,
                   max_health=1000, max_mana=200, max_energy=500,
                   sprite=EntitySprite(img_path="goblin.jpeg", scale=[50, 50]))
    game.set_player(player)
    game.spawn_entity(player)
    game.spawn_entity(npc)
    game.ping_everything()

    while True:
        time.sleep(1 / TPS)
        tick_graphics()
        game.tick()


run_game()
