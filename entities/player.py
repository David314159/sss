from entities.entity import Entity
from graphics import sprite


class Player(Entity):
    def __init__ (self):
        self.sprite = sprite.PlayerSprite()
        super().__init__("Player")

    def tick(self):
        super().tick()
