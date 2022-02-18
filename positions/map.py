from positions.base_grid import BaseGrid
from positions.region import Region


class Map(BaseGrid):
    def __init__(self, rows: int, cols: int):
        super().__init__(rows, cols)
        for row in range(0, rows):
            for col in range(0, cols):
                self.vals[row][col] = Region(5, 5)


global_map = Map(50, 50)
