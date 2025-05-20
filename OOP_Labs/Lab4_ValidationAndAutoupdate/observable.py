from typing import Protocol, Any
import change_listener


class Observable(change_listener.DataChangedProtocol):
    def __init__(self):
        # Changing through add/remove
        self._listeners: list[change_listener.PropertyChangedListenerProtocol] = []
    
    #region add/remove
    def add_property_changed_listener(self, 
                                      listener: change_listener.PropertyChangedListenerProtocol):
        if listener not in self._listeners:
            self._listeners.append(listener)
    
    def remove_property_changed_listener(self, 
                                         listener: change_listener.PropertyChangedListenerProtocol):
        if listener in self._listeners:
            self._listeners.remove(listener)
    #endregion
    
    def _notify_property_changed(self, property_name: str, 
                                 old_value: Any, new_value: Any):
        for listener in self._listeners:
            listener.on_property_changed(self, property_name, old_value, new_value)

class Validatable(Observable, change_listener.DataChangingProtocol):
    def __init__(self):
        super().__init__()
        # Changing through add/remove
        self._validators: list[change_listener.PropertyChangingListenerProtocol] = []
    
    #region add/remove
    def add_property_changing_listener(self,
                                       listener: change_listener.PropertyChangingListenerProtocol):
        if listener not in self._validators:
            self._validators.append(listener)
    
    def remove_property_changing_listener(self, 
                                          listener: change_listener.PropertyChangingListenerProtocol):
        if listener in self._validators:
            self._validators.remove(listener)
    #endregion

    def _validate_property_change(self, property_name: str, 
                                  old_value: Any, new_value: Any) -> bool:
        # Did any validator approved change
        return all(
            validator.on_property_changing(self, property_name, old_value, new_value)
            for validator in self._validators
        )