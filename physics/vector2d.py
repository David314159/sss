from math import sqrt
from math import cos, sin
from typing import Self


class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @staticmethod
    def from_tuple(coords: tuple[float, float]):
        return Vector2D(coords[0], coords[1])

    @staticmethod
    def from_polar(radius, angle):
        return Vector2D(radius*cos(angle), radius*sin(angle))

    def get_magnitude(self):
        return sqrt(self.x*self.x + self.y*self.y)

    def normalized(self):
        return self / self.get_magnitude()

    def __eq__(self, other: Self) -> Self:
        return (self.x, self.y) == (other.x, other.y)

    def __add__(self, other: Self) -> Self:
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self) -> Self:
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, by: float) -> Self:
        return Vector2D(self.x * by, self.y * by)

    def __truediv__(self, by: float) -> Self:
        return Vector2D(self.x / by, self.y / by)

    def __str__(self):
        return f"({self.x}, {self.y})"