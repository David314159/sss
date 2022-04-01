from entities.entity import Entity


class Signal:
    def __init__(self, sender: Entity):
        self.sender = sender


class MeleeAttack(Signal):
    def __init__(self, sender: Entity, weapon: str):
        # TODO make weapon not be a string lol
        super().__init__(sender)
        self.base_damage = 10
        self.weapon = weapon
