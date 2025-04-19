from typing import Self
from abc import ABC
from math import sqrt

class ABCVector(ABC):
    __slots__ = []

    def __init__(self):
        # No slots at abstract class
        pass
    
    # region getters/setters
    def __getitem__(self, key: int) -> float:
        return getattr(self, self.__slots__[key])

    def __setitem__(self, key: int, value: float) -> None:
        setattr(self, self.__slots__[key], value)
    # endregion

    # region iteration
    def __iter__(self):
        for slot in self.__slots__:
            yield getattr(self, slot)
    
    def __len__(self) -> int:
        return len(self.__slots__)
    # endregion
    
    # region operations
    def __eq__(self, other) -> bool:
        if len(self) != len(other): 
            return False  # There's no point to check vectors with different len
        for slot in self.__slots__:
            if getattr(self, slot) != getattr(other, slot):
                return False  # Checking every attribute by same slot at both vectors
        return True

    def __abs__(self) -> float:
        squared_sum = sum([getattr(self, slot)**2 for slot in self.__slots__])
        return sqrt(squared_sum)
    
    def __add__(self, other: Self) -> Self:
        new_vector = self.__class__()  # Creating instance with same type
        for slot in self.__slots__:
            value = getattr(self, slot) + getattr(other, slot)
            setattr(new_vector, slot, value)
        return new_vector
    
    def __sub__(self, other: Self) -> Self:
        new_vector = self.__class__()  # Creating instance with same type
        for slot in self.__slots__:
            value = getattr(self, slot) - getattr(other, slot)
            setattr(new_vector, slot, value)
        return new_vector
    
    def __mul__(self, other: float) -> Self:  # Multiplying by number
        new_vector = self.__class__()  # Creating instance with same type
        for slot in self.__slots__:
            value = getattr(self, slot) * other
            setattr(new_vector, slot, value)
        return new_vector
    
    def __truediv__(self, other: float) -> Self:  # Dividing by number
        new_vector = self.__class__()  # Creating instance with same type (mb i should do something with this copypasta)
        for slot in self.__slots__:
            value = getattr(self, slot) / other
            setattr(new_vector, slot, value)
        return new_vector
    
    def scalar_product(self, other: Self) -> float:
        result = 0  # FINALLY IT JUST CREATES COMMON FLOAT
        for slot in self.__slots__:
            value = getattr(self, slot) * getattr(other, slot)
            result += value
        return result
    # endregion

    def __str__(self):
        vector_type = type(self).__name__
        result = ', '.join(str(getattr(self, slot)) for slot in self.__slots__)
        return f"{vector_type}({result})"
    
    def __repr__(self): 
        result = ' '.join(str(getattr(self, slot)) for slot in self.__slots__)
        return result