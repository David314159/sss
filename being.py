from entity import Entity


class Being(Entity):
    def __init__(self, x_square: int, x_region: int, y_square: int, y_region: int, name: str, action_points: int):
        self.action_points = action_points
        super().__init__(x_square, x_region, y_square, y_region, name)
