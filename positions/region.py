from positions.base_grid import BaseGrid
from positions.square import Square


class Region(BaseGrid):
    def __init__(self, rows: int, cols: int):
        super().__init__(rows, cols)
        for row in range(0, rows):
            for col in range(0, cols):
                self.vals[row][col] = Square(col, row, set())

    def __repr__(self):
        return str(f"Region: {self.vals}")
