import time
from typing import Callable, Any, Sequence

import pygame

from entities.entity import Entity
from gameplay.action import GameAction
from gameplay.signal import Signal
from input import input
from pygame import time
from gameplay.clock import clock


class Game:
    def __init__(self, entities: set[Entity]):
        self.tick_num: int = 0
        self.entities = entities
        self.map = map
        self.keys_pressed: set = set()
        self.to_call_on_keypress: dict[int, set[Callable[[], Any]]] = {pygame.K_w: set(),
                                                                       pygame.K_a: set(),
                                                                       pygame.K_s: set(),
                                                                       pygame.K_d: set()}
        self.to_call_on_key_release: dict[int, set[Callable[[], Any]]] = {pygame.K_w: set(),
                                                                          pygame.K_a: set(),
                                                                          pygame.K_s: set(),
                                                                          pygame.K_d: set()}

    def tick(self):
        pygame.event.pump()
        input.update_pressed_keys()
        for entity in self.entities:
            entity.tick()
        clock.tick()

        old_keys_pressed = self.keys_pressed
        self.keys_pressed = input.detect_keys(*self.to_call_on_keypress.keys(),
                                        *self.to_call_on_key_release.keys())

        for key, funcs in self.to_call_on_keypress.items():
            for func in funcs:
                if key in self.keys_pressed and key not in old_keys_pressed:
                    func()
        for key, funcs in self.to_call_on_key_release.items():
            for func in funcs:
                if key in old_keys_pressed and key not in self.keys_pressed:
                    func()

        self.tick_num += 1

    def player_call_when_pressed(self, key: int, func: Callable[[], Any]):
        self.to_call_on_keypress[key].add(func)

    def player_call_when_released(self, key: int, func: Callable[[], Any]):
        self.to_call_on_key_release[key].add(func)

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
