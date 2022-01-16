class BaseGrid:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols

        self.vals = []
        for i in range(0, cols):
            self.vals.append([-1] * rows)

    def __str__(self):
        return str(self.vals)

    def set_val(self, x: int, y: int, val: int) -> None:
        self.vals[x][y] = val

    def get_val(self, x: int, y: int) -> int:
        return self.vals[x][y]