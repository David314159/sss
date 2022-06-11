import pygame

from entities.entity import Entity
from gameplay.action import GameAction, GameActionType
from graphics import sprite
from gameplay.actions.innate import punch

class Player(Entity):
    def __init__ (self, x_pos: int, y_pos: int, current_action = None, *args, **kwargs):
        self.sprite = sprite.PlayerSprite() # the player's avatar sprite
        self.action_slots = [None, None,
                             lambda: GameAction(GameActionType.ATTACK, 1000, lambda: punch(self)), None]

        super().__init__("Player", x_pos, y_pos, current_action, *args, **kwargs) # create an entity with these attributes

    def wasd_input(self, wasd_pressed: set[int]):
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

    def qe_input(self, qe_pressed: set[int]):
        if pygame.K_q in qe_pressed and self.action_slots[2] is not None:
            print("hi")
            self.current_action = self.action_slots[2]()
        if pygame.K_e in qe_pressed and self.action_slots[3] is not None:
            self.current_action = self.action_slots[3]()

    def tick(self):
        # update sprite position
        self.sprite.update_pos(self.x_pos, self.y_pos)
        print(f"x velocity: {self.x_velocity}")
        print(f"y velocity: {self.y_velocity}")

        super().tick()