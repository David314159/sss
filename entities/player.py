import pygame

from entities.entity import Entity
from gameplay.action import GameAction, GameActionType
from gameplay.actions.innate import punch
from graphics.sprite import EntitySprite


class Player(Entity):
    def __init__ (self, x_pos: int, y_pos: int, current_action = None, *args, **kwargs):
        self.action_slots = [None, None,
                             lambda: GameAction("Punch", GameActionType.ATTACK, 200, lambda: punch(self)), None]

        super().__init__(name="Player", x_pos=x_pos, y_pos=y_pos,
                         sprite=EntitySprite(img_path="captain_alex.png", scale=(40, 80)),
                         current_action=current_action,
                         *args, **kwargs)

    def set_action(self, action: GameAction):
        if self.current_action is None or self.current_action.name != action.name:
            self.current_action = action

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
            self.set_action(self.action_slots[2]())
        if pygame.K_e in qe_pressed and self.action_slots[3] is not None:
            self.set_action(self.action_slots[3]())
