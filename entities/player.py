from entities.entity import Entity
from graphics import sprite
from positions.directions import Direction


class Player(Entity):
    def __init__ (self, x_pos: int, y_pos: int, current_action = None):
        self.sprite = sprite.PlayerSprite()
        super().__init__("Player", x_pos, y_pos, current_action)

    def tick(self):
        super().tick()
