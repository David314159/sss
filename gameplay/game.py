from entities.entity import Entity
from gameplay.action import GameAction


class Game:
    def __init__(self, entities: list[Entity]):
        self.tick_num: int = 0
        self.actions: set[GameAction] = set()
        self.entities = entities

    def tick(self):
        for entity in self.entities:
            entity.tick()
        for action in self.actions:
            action.tick()
        self.tick_num += 1

    def action_started(self, action: GameAction):
        self.actions.add(action)

    def action_failed(self, action: GameAction):
        self.actions.remove(action)

    def entity_appears(self, entity: Entity):
        self.entities.append(entity)

    def entity_disappears(self, entity: Entity):
        self.entities.remove(entity)
