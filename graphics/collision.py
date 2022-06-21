from entities.entity import Entity
from graphics.sprite import entity_sprites
from pygame.sprite import spritecollide


def get_collisions(entity1: Entity):
    return spritecollide(entity1, entity_sprites)


