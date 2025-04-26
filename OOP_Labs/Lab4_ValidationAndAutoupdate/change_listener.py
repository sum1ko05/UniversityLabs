from typing import Protocol, Any


class PropertyChangedListenerProtocol(Protocol):
    def on_property_changed(obj: Any, property_name: str,
                            old_value: Any, new_value: Any):
        ...

class DataChangedProtocol(Protocol):
    def add_property_changed_listener(listener: PropertyChangedListenerProtocol):
        ...

    def remove_property_changed_listener(listener: PropertyChangedListenerProtocol):
        ...

class PropertyChangingListenerProtocol(Protocol):
    def on_property_changing(self, obj: Any, property_name: str, 
                             old_value: Any, new_value: Any) -> bool:
        ...

class DataChangingProtocol(Protocol):
    def add_property_changing_listener(self, listener: PropertyChangingListenerProtocol) -> None:
        ...
    def remove_property_changing_listener(self, listener: PropertyChangingListenerProtocol) -> None:
        ...