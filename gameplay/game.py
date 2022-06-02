from typing import Callable

import pygame

from entities.entity import Entity
from gameplay.action import GameAction
from gameplay.signal import Signal
from input import detect_wasd


class Game:
    def __init__(self, entities: set[Entity]):
        self.tick_num: int = 0
        self.entities = entities
        self.map = map

    def tick(self):
        for entity in self.entities:
            entity.tick()
        self.tick_num += 1

    def send_signal(self, signal: Signal, should_send_to: Callable[[Entity], bool]):
        for entity in self.entities:
            if should_send_to(entity):
                entity.handle_signal(signal)

    def ping_everything(self):
        game.send_signal(Signal(), lambda entity: True)

    def spawn_entity(self, entity: Entity):
        self.entities.add(entity)

    def despawn_entity(self, entity: Entity):
        self.entities.remove(entity)


game = Game(set())
