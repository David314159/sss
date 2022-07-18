from math import sqrt
from math import cos, sin

class Vector2D:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @staticmethod
    def from_tuple(coords: tuple[int, int]):
        return Vector2D(coords[0], coords[1])

    @staticmethod
    def from_polar(radius, angle):
        return Vector2D(radius*cos(angle), radius*sin(angle))

    def update(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_magnitude(self):
        return sqrt(self.x*self.x + self.y*self.y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
