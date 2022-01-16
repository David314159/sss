class Player:
    def __init__(self, x_region: int, y_region: int, x_square: int, y_square: int):
        self.x_region = x_region
        self.y_region = y_region
        self.x_square = x_square
        self.y_square = y_square

    def move_region(self, x_region: int, y_region: int):
        self.x_region = x_region
        self.y_region = y_region

    def move_square(self, x_square: int, y_square: int):
        self.x_square = x_square
        self.y_square = y_square
