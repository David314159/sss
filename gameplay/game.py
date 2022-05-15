from typing import Callable

from entities.entity import Entity
from gameplay.action import GameAction
from gameplay.signal import Signal
from positions import region
from positions.map import Map, global_map
from positions.region import Region

class Game:
    def __init__(self, entities: set[Entity], region: Region, map: Map):
        self.tick_num: int = 0
        self.entities = entities
        self.region = region
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

    def action_started(self, action: GameAction):
        self.actions.add(action)

    def action_failed(self, action: GameAction):
        self.actions.remove(action)

    def entity_appears(self, entity: Entity):
        self.entities.append(entity)

    def entity_disappears(self, entity: Entity):
        self.entities.remove(entity)

game = Game(set(), global_map.get_val(0, 0), global_map)
