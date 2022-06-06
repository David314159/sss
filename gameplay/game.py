from typing import Callable

import pygame

from entities.entity import Entity
from gameplay.signal import Signal
from input import input
from gameplay.clock import clock


class Game:
    def __init__(self, entities: set[Entity], player):
        self.tick_num: int = 0
        self.entities = entities
        self.map = map
        self.player = player
        self.keys_pressed: set = set()

    def tick(self):
        pygame.event.pump()
        input.update_keys_pressed()
        for entity in self.entities:
            entity.tick()
        clock.tick()

        self.player.player_wasd_input(input.detect_wasd())
        self.tick_num += 1

    def send_signal(self, signal: Signal, should_send_to: Callable[[Entity], bool]):
        for entity in self.entities:
            if should_send_to(entity):
                entity.handle_signal(signal)

    def ping_everything(self):
        self.send_signal(Signal(), lambda entity: True)

    def spawn_entity(self, entity: Entity):
        self.entities.add(entity)

    def despawn_entity(self, entity: Entity):
        self.entities.remove(entity)