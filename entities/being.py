from entities.entity import Entity


class Being(Entity):
    def __init__(self, x_square: int, x_region: int, y_square: int, y_region: int, name: str):
        self.action_points = 10
        self.MAX_ACTION_POINTS = 10
        super().__init__(x_square, x_region, y_square, y_region, name)
