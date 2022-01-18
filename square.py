from entity import Entity


class Square:
    def __init__(self, x: int, y: int, entities: list[Entity]):
        self.x = x
        self.y = y
        self.entities = entities