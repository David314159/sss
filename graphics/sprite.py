from typing import Callable, Any

import pygame

from graphics.window import screen

entity_sprites = pygame.sprite.Group()


# Sprites are for graphics and hitboxes


class EntitySprite(pygame.sprite.Sprite):
    def __init__(self, img_path: str, scale: tuple[int, int]):
        super().__init__()
        self.entity = None
        self.image = pygame.image.load(f"resources/images/sprites/{img_path}").convert()
        self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect()
        entity_sprites.add(self)

    def remove_entity_sprite(self):
        self.remove(entity_sprites)

    def tick(self):
        """Updates the sprite's position on the screen."""
        if self.entity is not None:
            self.rect.x = self.entity.x_pos
            self.rect.y = self.entity.y_pos


class ResourceBar:
    HEIGHT = 10
    GAP_SIZE = 5

    def __init__(self, entity: "Entity", attr_name: str, max_val: int, proximity_rank: int, color: tuple[int, int, int]):
        super().__init__()
        if max_val <= 0:
            raise Exception("Maximum value of a resource bar must be positive")
        self.entity = entity
        self.attr_name = attr_name
        self.max_val = max_val
        self.proximity_rank = proximity_rank
        self.color = color
        self.rect = pygame.Rect(0, 0, 0, 0)

    def tick(self):
        current_val = getattr(self.entity, self.attr_name)
        self.rect.width = self.entity.sprite.rect.width*(current_val/self.max_val)
        self.rect.left = self.entity.sprite.rect.left
        self.rect.bottom = self.entity.sprite.rect.top - (self.HEIGHT+self.GAP_SIZE)*self.proximity_rank
        self.rect.height = self.HEIGHT
        pygame.draw.rect(screen, self.color, self.rect)
