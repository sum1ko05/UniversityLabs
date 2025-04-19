# Win only!!
from typing import Self
import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# WIDTH = screensize[0]
# HEIGHT = screensize[1]
WIDTH = 1024
HEIGHT = 720


class Point2d:
    __slots__ = ['_x', '_y']

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # region getters/setters
    @property
    def x(self) -> float:
        return self._x
    
    @x.setter
    def x(self, value: float):
        if 0 <= value <= WIDTH:
            self._x = value
        else:  # Don't allow to change value if it'll make point outside of screen
            raise ValueError("Position is out of valid range")
    
    @property
    def y(self) -> float:
        return self._y
    
    @y.setter
    def y(self, value: float):
        if 0 <= value <= HEIGHT:
            self._y = value
        else:  # Don't allow to change value if it'll make point outside of screen
            raise ValueError("Position is out of valid range")
    # endregion

    def __eq__(self, other: Self) -> bool:  # Returns true if self == other
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        result = ', '.join(str(getattr(self, slot)) for slot in self.__slots__)
        return f"Point({result})"
    
    def __repr__(self): 
        result = ' '.join(str(getattr(self, slot)) for slot in self.__slots__)
        return result