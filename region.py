from base_grid import BaseGrid


class Region(BaseGrid):
    def __init__(self, rows: int, cols: int):
        super().__init__(rows, cols, -1)

    def __repr__(self):
        return str(f"Region: {self.vals}")
