from point2d import Point2d
from vector import ABCVector

class Vector2d(ABCVector):
    __slots__ = ["_x", "_y"]

    def __init__(self, x: float = 0, y: float = 0):
        super().__init__()
        self.x = x
        self.y = y
    
    @classmethod  # Second constructor
    def from_point2d(cls, start: Point2d, end: Point2d):
        return cls(end.x - start.x, end.y - start.y)
    
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
    # endregion

    # already iterable
    
    # no new operations
