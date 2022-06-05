import pygame

from entities.entity import Entity
from graphics import sprite
from positions.directions import Direction
from gameplay.game import game
from math import ceil, sqrt

class Player(Entity):
    def __init__ (self, x_pos: int, y_pos: int, current_action = None):
        self.sprite = sprite.PlayerSprite()\

        # W
        game.player_call_when_pressed(pygame.K_w, lambda: self.start_moving(Direction.NORTH))
        game.player_call_when_released(pygame.K_w, lambda: self.stop_moving())
        # A
        game.player_call_when_pressed(pygame.K_a, lambda: self.start_moving(Direction.WEST))
        game.player_call_when_released(pygame.K_a, lambda: self.stop_moving())
        # S
        game.player_call_when_pressed(pygame.K_s, lambda: self.start_moving(Direction.SOUTH))
        game.player_call_when_released(pygame.K_s, lambda: self.stop_moving())
        # D
        game.player_call_when_pressed(pygame.K_d, lambda: self.start_moving(Direction.EAST))
        game.player_call_when_released(pygame.K_d, lambda: self.stop_moving())

        super().__init__("Player", x_pos, y_pos, current_action)


    def start_moving(self, direction: Direction):
        match direction:
            case Direction.NORTH:
                self.set_x_velocity(self.speed)
            case Direction.NORTHEAST:
                self.set_x_velocity(ceil(self.speed / sqrt(2)))
                self.set_y_velocity(ceil(self.speed / sqrt(2)))
            case Direction.EAST:
                self.set_x_velocity(self.speed)
            case Direction.SOUTHEAST:
                self.set_x_velocity(ceil(self.speed / sqrt(2)))
                self.set_y_velocity(-ceil(self.speed / sqrt(2)))
            case Direction.SOUTH:
                self.set_y_velocity(-self.speed)
            case Direction.SOUTHWEST:
                self.set_x_velocity(-ceil(self.speed / sqrt(2)))
                self.set_y_velocity(-ceil(self.speed / sqrt(2)))
            case Direction.WEST:
                self.set_x_velocity((-self.speed))
            case Direction.NORTHWEST:
                self.set_x_velocity(-ceil(self.speed / sqrt(2)))
                self.set_y_velocity(ceil(self.speed / sqrt(2)))

    def stop_moving(self):
        self.set_velocity(0, 0)

    def tick(self):
        super().tick()

