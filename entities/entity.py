from positions.region import Region
from positions.square import Square
from positions.map import global_map


class Entity:
    def __init__(self, x_square: int, x_region: int, y_square: int, y_region: int, name: str, current_action = None):
        self.x_region = x_region
        self.y_region = y_region
        self.x_square = x_square
        self.y_square = y_square
        self.current_action = current_action

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

    def tick(self):
        if self.current_action is not None:
            if self.current_action.is_finished():
                self.current_action = None
            else:
                self.current_action.tick()


