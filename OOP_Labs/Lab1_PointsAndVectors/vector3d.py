from typing import Self
from vector import ABCVector
from vector2d import Vector2d

class Vector3d(ABCVector):
    __slots__ = ["_x", "_y", "_z"]

    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z
    
    @classmethod  # Second constructor
    def from_vector2d(cls, vector: Vector2d):
        return cls(vector.x, vector.y)
    
    # region getters/setters
    @property
    def x(self) -> float:
        return self._x
    
    @x.setter
    def x(self, value: float):
        self._x = value

    @property
    def y(self) -> float:
        return self._y
    
    @y.setter
    def y(self, value: float):
        self._y = value

    @property
    def z(self) -> float:
        return self._z
    
    @z.setter
    def z(self, value: float):
        self._z = value
    # endregion

    # already iterable
    
    # region operations
    @classmethod
    def vector_product(cls, first: Self, second: Self) -> Self:
        # Just calculate determinant
        return cls(first.y*second.z - first.z*second.y,
                   first.x*second.z - first.z*second.x,
                   first.x*second.y - first.y*second.x)
                        
    @classmethod
    def triple_product(cls, first: Self, second: Self, third: Self) -> float:
        return first.scalar_product(cls.vector_product(second, third))
    # endregion
