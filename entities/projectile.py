from entities.entity import Entity
from gameplay.clock import clock
from graphics.sprite import ProjectileSprite, EntitySprite
from graphics.collision import get_collisions
from physics.vector2d import Vector2D


class Projectile(Entity):
    def __init__(self, name: str, duration: int, source: Entity, position: Vector2D, sprite: ProjectileSprite, initial_velocity: Vector2D, *args, **kwargs):
        self.source = source
        self.colliding_entities = []
        self.start_time = None
        self.duration = duration
        super().__init__(name=name, position=position, sprite=sprite, initial_velocity=initial_velocity, *args, **kwargs)

    def on_collide(self, target: Entity):
        print(f"I am colliding with {id(target)}")

    def should_die(self) -> bool:
        if any(self.colliding_entities):
            return True
        if clock.time - self.start_time > self.duration:
            return True
        return super().should_die()

    def first_tick(self):
        self.start_time = clock.time

    def tick(self):
        self.colliding_entities = [sprite for sprite in
                                   get_collisions(self, should_exclude=
                                                  lambda entity: entity is self.source.sprite)
                                   if sprite is not self]
        for entity_sprite in self.colliding_entities:
            self.on_collide(entity_sprite.entity)

        super().tick()
