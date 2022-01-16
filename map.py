from base_grid import BaseGrid
from region import Region


class Map(BaseGrid):
    def __init__(self, rows: int, cols: int):
        super().__init__(rows, cols, Region(5, 5))
