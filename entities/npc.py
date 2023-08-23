from entities.being import Being
from gameplay.game import game
from physics.vector2d import Vector2D


class NPC(Being):
    """Will add more to this later"""

    def tick(self):
        npc_to_player: Vector2D = game.player.position - self.position
        if npc_to_player == Vector2D(0, 0):
            self.velocity = Vector2D(0, 0)
        else:
            self.velocity = npc_to_player.normalized() * self.speed
        super().tick()



