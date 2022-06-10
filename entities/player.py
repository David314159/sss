import pygame

from entities.entity import Entity
from graphics import sprite

class Player(Entity):
    def __init__ (self, x_pos: int, y_pos: int, current_action = None):
        self.sprite = sprite.PlayerSprite() # the player's avatar sprite

        super().__init__("Player", x_pos, y_pos, current_action) # create an entity with these attributes


    def player_wasd_input(self, wasd_pressed: set):
        # handles the player's WASD input for moving

        self.set_velocity(0, 0) # set the velocity to zero each time
        # if the player is in control of their movement and they do nothing,
        # this will ensure they don't move
        if pygame.K_w in wasd_pressed:
            self.y_velocity -= self.speed
        if pygame.K_a in wasd_pressed:
            self.x_velocity -= self.speed
        if pygame.K_s in wasd_pressed:
            self.y_velocity += self.speed
        if pygame.K_d in wasd_pressed:
            self.x_velocity += self.speed


    def tick(self):

        # update sprite position
        self.sprite.update_pos(self.x_pos, self.y_pos)

        super().tick()

