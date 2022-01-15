from array import *


class Grid:
    def __init__(self, rows, cols):
        self.rows = rows;
        self.cols = cols;

        self.vals = []
        for i in range(0, cols):
            self.vals.append([])
            for j in range(0, rows):
                self.vals[i].append(-1)

    def __str__(self):
        return str(self.vals)

    def set_val(self, x, y, val):
        self.vals[x][y] = val

    def get_val(self, x, y, val):
        return self.vals[x][y]
