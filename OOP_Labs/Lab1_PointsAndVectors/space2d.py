# Win only!!
import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

WIDTH = screensize[0]
HEIGHT = screensize[1]

from math import sqrt

class Point2d:
    def __init__(self, x: int, y: int):
        self._prop = list()
        # Clamping points to value between 0 and WIDTH/HEIGHT
        self._prop.append(max(0, min(x, WIDTH)))
        self._prop.append(max(0, min(y, HEIGHT)))

    # region getters/setters
    @property
    def x(self) -> int:
        return self._prop[0]
    
    @x.setter
    def x(self, value: int):
        if 0 <= value <= WIDTH:
            self._prop[0] = value
        else: # Don't allow to change value if it'll make point outside of screen
            raise(ValueError)
    
    @property
    def y(self) -> int:
        return self._prop[1]
    
    @y.setter
    def y(self, value: int):
        if 0 <= value <= HEIGHT:
            self._prop[1] = value
        else: # Don't allow to change value if it'll make point outside of screen
            raise(ValueError)
    # endregion

    def __eq__(self, other): # Returns true if self == other
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        result = ', '.join(str(x) for x in self._prop)
        return f"Point({result})"
    
    def __repr__(self): 
        result = ' '.join(str(x) for x in self._prop)
        return result

class Vector2d:
    def __init__(self, x: int, y: int):
        self._prop = list()
        self._prop.append(x)
        self._prop.append(y)
    
    @classmethod # Second constructor
    def set_by_points(cls, start: Point2d, end: Point2d):
        return cls(end.x - start.x, end.y - start.y)
    
    # region getters/setters
    def __getitem__(self, key: int):
        return self._prop[key]

    def __setitem__(self, key: int, value: int):
        self._prop[key] = value
    # endregion

    # region iteration
    def __iter__(self):
        return iter(self._prop)
    
    def __len__(self):
        return self._prop
    # endregion
    
    # region operations
    def __eq__(self, other) -> bool:
        return self._prop == other._prop

    def __abs__(self) -> int:
        squared_sum = sum([x**2 for x in self._prop])
        return sqrt(squared_sum)
    
    def __add__(self, other) -> 'Vector2d':
        result = [x + y for x, y in zip(self._prop, other._prop)]
        return Vector2d(result[0], result[1])
    
    def __sub__(self, other) -> 'Vector2d':
        result = [x - y for x, y in zip(self._prop, other._prop)]
        return Vector2d(result[0], result[1])
    
    def __mul__(self, other: int) -> 'Vector2d': # Multiplying by number
        result = [x * other for x in self._prop]
        return Vector2d(result[0], result[1])
    
    def __truediv__(self, other: int) -> 'Vector2d': # Dividing by number
        result = [x / other for x in self._prop]
        return Vector2d(result[0], result[1])
    
    def scalar_product(self, other) -> int:
        result = sum([x * y for x, y in zip(self._prop, other._prop)])
        return result
    
    # Vector and triple products are not defined in 2d space
    # endregion

    def __str__(self):
        result = ', '.join(str(x) for x in self._prop)
        return f"Vector({result})"
    
    def __repr__(self): 
        result = ' '.join(str(x) for x in self._prop)
        return result

class Vector3d(Vector2d):
    def __init__(self, x: int, y: int, z: int):
        self._prop = list()
        self._prop.append(x)
        self._prop.append(y)
        self._prop.append(z)
    
    @classmethod # Second constructor
    def set_by_points(cls, start: Point2d, end: Point2d):
        return cls(end.x - start.x, end.y - start.y, 0)
    
    @classmethod # Convert from Vector2d
    def from_2d(cls, vector):
        return cls(vector[0], vector[1], 0)
    
    # already can get/set item and already iterable

    # region operations
    def __add__(self, other) -> 'Vector3d':
        result = [x + y for x, y in zip(self._prop, other._prop)]
        return Vector3d(result[0], result[1], result[2])
    
    def __sub__(self, other) -> 'Vector3d':
        result = [x - y for x, y in zip(self._prop, other._prop)]
        return Vector3d(result[0], result[1], result[2])
    
    def __mul__(self, other: int) -> 'Vector3d': # Multiplying by number
        result = [x * other for x in self._prop]
        return Vector3d(result[0], result[1], result[2])
    
    def __truediv__(self, other: int) -> 'Vector3d': # Dividing by number
        result = [x / other for x in self._prop]
        return Vector3d(result[0], result[1], result[2])
    
    @classmethod
    def vector_product(cls, first: 'Vector3d', second: 'Vector3d') -> 'Vector3d':
        # Just calculate determinant
        return Vector3d(first[1]*second[2] - first[2]*second[1],
                        first[0]*second[2] - first[2]*second[0],
                        first[0]*second[1] - first[1]*second[0])

    @classmethod
    def triple_product(cls, first: 'Vector3d', second: 'Vector3d', third: 'Vector3d') -> int:
        return first.scalar_product(Vector3d.vector_product(second, third))
    # endregion