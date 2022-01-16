class BaseGrid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.vals = []
        for i in range(0, cols):
            self.vals.append([-1] * rows)

    def __str__(self):
        return str(self.vals)

    def set_val(self, x, y, val):
        self.vals[x][y] = val

    def get_val(self, x, y):
        return self.vals[x][y]