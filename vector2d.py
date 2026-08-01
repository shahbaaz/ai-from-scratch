
from typing import Self
from math import sqrt


class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"
    
    def __add__(self, other: Self) -> Vector2D:
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: Self):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other: float):
        return Vector2D(self.x * other, self.y * other)
    
    def __rmul__(self, other: float):
        return Vector2D(other * self.x, other * self.y)
    
    def __eq__(self, value: object) -> bool:
        if (type(value) != Vector2D):
            return False
        return self.x == value.x and self.y == value.y
        
    def __abs__(self) -> float:
        return sqrt(self.x**2 + self.y**2)