from typing import Any


class BaseGrid:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.vals = []
        for row in range(0, rows):
            self.vals.append([])
            for col in range(0, cols):
                self.vals[row].append(None)

    def __str__(self) -> str:
        return str(self.vals)

    def set_val(self, x: int, y: int, val: Any) -> None:
        self.vals[x][y] = val

    def get_val(self, x: int, y: int) -> Any:
        return self.vals[x][y]
