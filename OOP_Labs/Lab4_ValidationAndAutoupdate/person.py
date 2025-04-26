from typing import Protocol, Any
import change_listener
from observable import Observable, Validable
from logger.logger import Logger


class Person(Validable):
    def __init__(self, name: str, age: int):
        super().__init__()
        self._name = name
        self._age = age
    
    #region properties:
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        if self._validate_property_change('name', self._name, value):
            old = self._name
            self._name = value
            self._notify_property_changed('name', old, self._name)
    
    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, value: int) -> None:
        if self._validate_property_change('age', self._age, value):
            old = self._age
            self._age = value
            self._notify_property_changed('age', old, self._age)
    #endregion

    def __str__(self):
        return f'Name: {self.name} \t Age: {self.age}'

#region validators
class CommonAgeValidator(change_listener.PropertyChangingListenerProtocol):
    def on_property_changing(self, obj: Any, property_name: str, 
                             old_value: int, new_value: int) -> bool:
        if property_name == 'age':
            if new_value < 0:
                print(f"Error: Age cannot be negative! Remaining {old_value} for {obj}")
                return False
            if new_value > 120:
                print(f"Error: Age cannot be more than 120! Remaining {old_value} for {obj}")
                return False
        return True
    
class MinorAgeValidator(change_listener.PropertyChangingListenerProtocol):
    def on_property_changing(self, obj: Any, property_name: str, 
                             old_value: int, new_value: int) -> bool:
        if property_name == 'age':
            if new_value < 0:
                print(f"Error: Age cannot be negative! Remaining {old_value} for {obj}")
                return False
            if new_value > 17:
                print(f"Error: Don't try to fool the system! Remaining {old_value} for {obj}")
                return False
        return True

class NameValidator(change_listener.PropertyChangingListenerProtocol):
    def on_property_changing(self, obj: Any, property_name: str, 
                             old_value: str, new_value: str) -> bool:
        if property_name == 'name':
            if not new_value.isalpha():
                print(f"Error: Name must contain only letters! Remaining {old_value} for {obj}")
                return False
            if len(new_value) < 2:
                print(f"Error: Name too short! Remaining {old_value} for {obj}")
                return False
        return True
#endregion

class PropertyLogger(change_listener.PropertyChangedListenerProtocol):
    def __init__(self, logger: Logger):
        self.logger = logger

    def on_property_changed(self, obj, property_name, old_value, new_value):
        self.logger.log(f'Info: {property_name} was changed in {obj} from {old_value} to {new_value}')