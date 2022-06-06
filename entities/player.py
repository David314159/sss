import pygame

from entities.entity import Entity
from graphics import sprite

class Player(Entity):
    def __init__ (self, x_pos: int, y_pos: int, current_action = None):
        self.sprite = sprite.PlayerSprite()

        super().__init__("Player", x_pos, y_pos, current_action)


    def player_wasd_input(self, wasd_pressed: set):
        self.set_velocity(0, 0)
        if pygame.K_w in wasd_pressed:
            self.y_velocity += self.speed
        if pygame.K_a in wasd_pressed:
            self.x_velocity -= self.speed
        if pygame.K_s in wasd_pressed:
            self.y_velocity -= self.speed
        if pygame.K_d in wasd_pressed:
            self.x_velocity += self.speed


    def tick(self):
        super().tick()

