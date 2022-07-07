from entities.projectile import Projectile
from gameplay.signal import Signal


class Punch(Projectile):
    def on_collide(self, target: "Entity"):
        signal = Signal(sender = self, damage = 100, damage_type = "Normal")
        target.handle_signal(signal)
