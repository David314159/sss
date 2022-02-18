from typing import Collection, Any


class Square:
    def __init__(self, x: int, y: int, entities: set[Any]):
        self.x = x
        self.y = y
        self.entities = entities
