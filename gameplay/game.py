from typing import Callable

import pygame

from entities.entity import Entity
from gameplay.signal import Signal
from input import input
from gameplay.clock import clock


class Game:
    def __init__(self, entities: set[Entity]):
        # main game class
        # keeps track of entities loaded, signals, and the current gamestate
        self.tick_num: int = 0 # number of game ticks since the game was launched
        self.entities = entities # the set of entities in the game
        self.player = None
        self.keys_pressed: set = set() # keys pressed right now

    def set_player(self, player):
        self.player = player

    def tick(self):
        pygame.event.pump() # allows key input and graphics to change
        input.tick()
        for entity in self.entities:
            entity.tick()
        clock.tick()

        self.player.wasd_input(input.detect_wasd()) # take player WASD input
        # this will get more complicated once things affect player input (menus, ect)
        self.player.qe_input(input.detect_qe())

        self.tick_num += 1

    def send_signal(self, signal: Signal, should_send_to: Callable[[Entity], bool]):
        # our game's event system. This allows any object to send a custom object that is received and
        # interpreted by any number of entities that satisfy a condition
        for entity in self.entities:
            if should_send_to(entity):
                entity.handle_signal(signal)

    def ping_everything(self):
        # sends an empty singal to everything
        self.send_signal(Signal(), lambda entity: True)

    def spawn_entity(self, entity: Entity):
        # load an entity
        self.entities.add(entity)

    def despawn_entity(self, entity: Entity):
        # unload an entity
        self.entities.remove(entity)


game = Game(set())
