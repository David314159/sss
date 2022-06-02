from positions.directions import Direction
from gameplay.signal import Signal


class Entity:
    def __init__(self, name: str, x_pos: int, y_pos: int, current_action = None):

        # Lasting, constant attributes
        self.name = name

        # Lasting, variable attributes
        self.x_pos = x_pos
        self.y_pos = y_pos

        # Temporary states
        self.current_action = current_action
        self.moving = False
        self.direction_moving = None

        # Stats
        self.speed = 5

    def tick(self):
        if self.current_action is not None:
            if self.current_action.finished:
                self.current_action = None
            else:
                self.current_action.tick()

    def handle_signal(self, signal: Signal):
        print("I am handling signal", signal)
