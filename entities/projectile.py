from entities.entity import Entity
from gameplay.clock import clock
from graphics.sprite import ProjectileSprite, EntitySprite
from graphics.collision import get_collisions
from physics.vector2d import Vector2D


class Projectile(Entity):
    def __init__(self, name: str, duration: int, source: Entity, position: Vector2D, sprite: ProjectileSprite, initial_velocity: Vector2D, *args, **kwargs):
        self.source = source
        self.start_time = None
        self.duration = duration
        super().__init__(name=name, position=position, sprite=sprite, initial_velocity=initial_velocity, *args, **kwargs)

    def on_collide(self, target: Entity):
        print(f"I, {self.name}, collided with {target.name}")

    def first_tick(self):
        self.start_time = clock.time

    def should_die(self) -> bool:
        if clock.time - self.start_time > self.duration:
            return True
        else:
            return super().should_die()

    def tick(self):
        colliding_entities = filter(lambda sprite: isinstance(sprite, EntitySprite), get_collisions(self))
        for entity_sprite in colliding_entities:
            self.on_collide(entity_sprite.entity)
        super().tick()
