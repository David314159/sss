import pygame

from entities.entity import Entity
from gameplay import ability
from gameplay.action import nothing_action
from graphics.sprite import EntitySprite


class Player(Entity):
    """The player of the game. There should only be one of these (for now)."""
    def __init__ (self, x_pos: int, y_pos: int, current_action=nothing_action, *args, **kwargs):
        self.ability_slots = [ability.empty_slot, ability.empty_slot,
                              ability.punch, ability.empty_slot]

        super().__init__(name="Player", x_pos=x_pos, y_pos=y_pos,
                         sprite=EntitySprite(img_path="captain_alex.png", scale=[40, 80]),
                         current_action=current_action,
                         *args, **kwargs)

    def wasd_input(self, wasd_pressed: set[int]):
        """Handles the player's WASD input for moving.
        wasd_pressed is the set of WASD keys that are currently pressed."""

        # set the velocity to zero each time
        # if the player is in control of their movement and they do nothing,
        # this will ensure they don't move
        self.set_velocity(0, 0)

        if self.current_action.can_move:
            if pygame.K_w in wasd_pressed:
                self.y_velocity -= self.speed
            if pygame.K_a in wasd_pressed:
                self.x_velocity -= self.speed
            if pygame.K_s in wasd_pressed:
                self.y_velocity += self.speed
            if pygame.K_d in wasd_pressed:
                self.x_velocity += self.speed

    def qe_input(self, qe_pressed: set[int]):
        """Handles the player's QE input for abilities."""
        if pygame.K_q in qe_pressed:
            self.attempt_ability(self.ability_slots[2])
        if pygame.K_e in qe_pressed:
            self.attempt_ability(self.ability_slots[3])
