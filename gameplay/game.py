from entities.entity import Entity
from gameplay.action import GameAction
from positions import region
from positions.map import Map
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

    def action_started(self, action: GameAction):
        self.actions.add(action)

    def action_failed(self, action: GameAction):
        self.actions.remove(action)

    def entity_appears(self, entity: Entity):
        self.entities.append(entity)

    def entity_disappears(self, entity: Entity):
        self.entities.remove(entity)
