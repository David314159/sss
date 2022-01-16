from directions import Direction


class Player:
    def __init__(self, x_region: int, y_region: int, x_square: int, y_square: int):
        self.x_region = x_region
        self.y_region = y_region
        self.x_square = x_square
        self.y_square = y_square
        self.action_points = 10

    def move_squares(self, direction: Direction, num_squares: int):
        match direction:
            case Direction.NORTH:
                self.y_square += num_squares
            case Direction.EAST:
                self.x_square += num_squares
            case Direction.WEST:
                self.x_square -= num_squares
            case Direction.SOUTH:
                self.y_square -= num_squares
