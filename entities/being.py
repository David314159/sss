from entities.entity import Entity
from gameplay.signal import Signal, MeleeAttack


class Being(Entity):
    def __init__(self, x_square: int, x_region: int, y_square: int, y_region: int, name: str):
        self.busy = False
        super().__init__(x_square, x_region, y_square, y_region, name)

    def attack(self, weapon: str):


    def receive_signal(self, signal: Signal):
        if isinstance(signal, MeleeAttack):
            print("ow")
