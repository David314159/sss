class Signal:
    def __init__(self, sender: "Entity" = None, damage: int = None, damage_type: str = None, ):
        self.sender = sender

        self.damage = damage
        self.damage_type = damage_type
        # examples of what a signal could contain
