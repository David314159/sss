from math import sqrt

class Vector2D:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def update(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_magnitude(self):
        return sqrt(self.x*self.x + self.y*self.y)

