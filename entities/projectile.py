from entities.entity import Entity
from graphics.sprite import ProjectileSprite
from physics.vector2d import Vector2D


class Projectile(Entity):
    def __init__(self, source: Entity, position: Vector2D, sprite: ProjectileSprite, initial_velocity: Vector2D, *args, **kwargs):
        self.source = source
        super().__init__(position=position, sprite=sprite, initial_velocity=initial_velocity, *args, **kwargs)

    def on_collide(self, target: Entity):
        pass

    def tick(self):
        pass