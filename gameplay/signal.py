from entities import entity

current_signals = set()

class Signal:
    """An info class representing an effect on an entity. Sent to entities through their handle_signal method."""
    class NegativeDamageException(Exception):
        pass

    def __init__(self, sender: "entity.Entity" = None, damage: int = 0, damage_type: str = None, ):
        if damage is not None and damage < 0:
            # Negative damage should never be in the game
            raise self.NegativeDamageException("Damage cannot be negative")

        self.sender = sender

        self.damage = damage
        self.damage_type = damage_type
        # examples of what a signal could contain

