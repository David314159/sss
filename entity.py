from directions import Direction
from map import global_map
from region import Region
from square import Square


class Entity:
    def __init__(self, x_square: int, x_region: int, y_square: int, y_region: int, name: str):
        self.x_region = x_region
        self.y_region = y_region
        self.x_square = x_square
        self.y_square = y_square

        new_region: Region = global_map.get_val(self.x_region, self.y_region)
        new_square: Square = new_region.get_val(self.x_square, self.y_square)
        new_square.entities.add(self)

        self.name = name

    def update_square(self, x_square, y_square):
        # Remove entity from current square
        current_region: Region = global_map.get_val(self.x_region, self.y_region)
        current_square: Square = current_region.get_val(self.x_square, self.y_square)
        current_square.entities.remove(self)

        # Update variables
        self.x_square = x_square
        self.y_square = y_square

        # Add entity to new square
        new_region: Region = global_map.get_val(self.x_region, self.y_region)
        new_square: Square = new_region.get_val(self.x_square, self.y_square)
        new_square.entities.add(self)

    def move_squares(self, direction: Direction, num_squares: int):
        match direction:
            case Direction.NORTH:
                self.update_square(self.x_square, self.y_square + num_squares)
            case Direction.EAST:
                self.update_square(self.x_square + num_squares, self.y_square)
            case Direction.WEST:
                self.update_square(self.x_square - num_squares, self.y_square)
            case Direction.SOUTH:
                self.update_square(self.x_square, self.y_square - num_squares)
            case Direction.NORTHEAST:
                self.move_squares(Direction.NORTH, num_squares)
                self.move_squares(Direction.EAST, num_squares)
            case Direction.SOUTHEAST:
                self.move_squares(Direction.SOUTH, num_squares)
                self.move_squares(Direction.EAST, num_squares)
            case Direction.NORTHWEST:
                self.move_squares(Direction.NORTH, num_squares)
                self.move_squares(Direction.WEST, num_squares)
            case Direction.SOUTHWEST:
                self.move_squares(Direction.SOUTH, num_squares)
                self.move_squares(Direction.WEST, num_squares)
