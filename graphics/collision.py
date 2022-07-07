from typing import Callable

from entities.entity import Entity
from graphics.sprite import entity_sprites
from pygame.sprite import spritecollide
from pygame.sprite import collide_rect


def get_collisions(entity1: Entity, should_exclude: Callable[["Entity"], bool]):
    return spritecollide(entity1.sprite, entity_sprites, False,
                         collided=
                         lambda sprite1, sprite2: collide_rect(sprite1, sprite2) \
                                                  and sprite1 is not sprite2 \
                                                  and not should_exclude(sprite1) and not should_exclude(sprite2))
