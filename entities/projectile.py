from entities.entity import Entity
from graphics.sprite import ProjectileSprite, EntitySprite
from graphics.collision import get_collisions
from physics.vector2d import Vector2D


class Projectile(Entity):
    def __init__(self, name: str, source: Entity, position: Vector2D, sprite: ProjectileSprite, initial_velocity: Vector2D, *args, **kwargs):
        self.source = source
        super().__init__(name=name, position=position, sprite=sprite, initial_velocity=initial_velocity, *args, **kwargs)

    def on_collide(self, target: Entity):
        print(f"I, {self.name}, collided with {target.name}")

    def tick(self):
        colliding_entities = filter(lambda sprite: isinstance(sprite, EntitySprite), get_collisions(self))
        for entity_sprite in colliding_entities:
            self.on_collide(entity_sprite.entity)
        super().tick()
