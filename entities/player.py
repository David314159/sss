import pygame

from entities.entity import Entity
from graphics import sprite
from positions.directions import Direction
from math import sqrt, ceil
from gameplay.game import game

class Player(Entity):
    def __init__ (self, x_pos: int, y_pos: int, current_action = None):
        self.sprite = sprite.PlayerSprite()
        game.player_call_when_pressed(pygame.K_w, lambda: self.start_moving(Direction.NORTH))
        game.player_call_when_released(pygame.K_w, lambda: self.stop_moving())
        super().__init__("Player", x_pos, y_pos, current_action)

    def move(self, direction: Direction):
        match direction:
            case Direction.NORTH:
                self.y_pos += self.speed
            case Direction.NORTHEAST:
                self.x_pos += ceil(self.speed/sqrt(2))
                self.y_pos += ceil(self.speed/sqrt(2))
            case Direction.EAST:
                self.x_pos += self.speed
            case Direction.SOUTHEAST:
                self.x_pos += ceil(self.speed/sqrt(2))
                self.y_pos -= ceil(self.speed/sqrt(2))
            case Direction.SOUTH:
                self.y_pos -= self.speed
            case Direction.SOUTHWEST:
                self.x_pos -= ceil(self.speed/sqrt(2))
                self.y_pos -= ceil(self.speed/sqrt(2))
            case Direction.WEST:
                self.x_pos -= self.speed
            case Direction.NORTHWEST:
                self.x_pos += ceil(self.speed / sqrt(2))
                self.y_pos += ceil(self.speed / sqrt(2))
            case direction.SOUTH:
                self.y_pos -= self.speed


    def start_moving(self, direction: Direction):
        self.call_continuously("player move", lambda: self.move(direction), 50)

    def stop_moving(self):
        func_specs_to_remove = set()
        for func_spec in self.to_call_continuously:
            if func_spec.name == "player move":
                func_specs_to_remove.add(func_spec)
        for func_spec in func_specs_to_remove:
            self.to_call_continuously.remove(func_spec)

    def tick(self):
        super().tick()

