from typing import Any


class BaseGrid:
    def __init__(self, rows: int, cols: int, default_value: Any = None):
        self.rows = rows
        self.cols = cols
        self.vals = [([default_value] * cols)] * rows

    def __str__(self) -> str:
        return str(self.vals)

    def set_val(self, x: int, y: int, val: Any) -> None:
        self.vals[x][y] = val

    def get_val(self, x: int, y: int) -> int:
        return self.vals[x][y]
