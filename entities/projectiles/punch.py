from entities.projectile import Projectile


class Punch(Projectile):

    def on_collide(self, target: "Entity"):
        super().on_collide(target)
        passw