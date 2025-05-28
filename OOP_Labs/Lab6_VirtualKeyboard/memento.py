from virtual_receiver import VirtualReceiver
from typing import Protocol
import json
from virtual_receiver import ReceiverMemento


class MementoManagerProtocol(Protocol):
    def save_state(self):
        ...

    def load_state(self):
        ...

    def undo(self):
        ...

    def redo(self):
        ...


class MemoryMementoManager(MementoManagerProtocol):
    def __init__(self, receiver: VirtualReceiver):
        self.receiver = receiver
        self.current_memento = self.receiver.create_memento()
        self.undo_stack = list()
        self.redo_stack = list()

    def save_state(self):
        self.undo_stack.append(self.current_memento)
        self.redo_stack.clear()
        self.current_memento = self.receiver.create_memento()

    def load_state(self):
        pass  # Not suitable for memory-only implementation

    def undo(self):
        if not self.undo_stack: # Is undo_stack empty
            print("No states before was found")
            return
        self.redo_stack.append(self.current_memento)
        self.current_memento = self.undo_stack.pop()
        self.receiver.load_memento(self.current_memento)

    def redo(self):
        if not self.redo_stack: # Is redo_stack empty
            print("No states after was found")
            return
        self.undo_stack.append(self.current_memento)
        self.current_memento = self.redo_stack.pop()
        self.receiver.load_memento(self.current_memento)


class JSONMementoManager(MementoManagerProtocol):
    def __init__(self, receiver: VirtualReceiver, file_path: str):
        self.receiver = receiver
        self.file_path = file_path
        self.current_memento = self.receiver.create_memento()
        self.undo_stack = list()
        self.redo_stack = list()

    def _load_data(self):
        try:
            with open(self.file_path, 'r') as f:
                json_dict = json.load(f)
                # print(json_dict)
                self.current_memento = ReceiverMemento(json_dict["current_memento"])
                self.undo_stack = [ReceiverMemento(data) for data in json_dict["undo_stack"]]
                self.redo_stack = [ReceiverMemento(data) for data in json_dict["redo_stack"]]
                # self.receiver.load_memento(ReceiverMemento(memento_dict))
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as error:
            raise error  # No memento found
        
    def _save_data(self):
        try:
            with open(self.file_path, 'w') as file:
                json.dump({
                            "current_memento": self.current_memento.get_state(),
                            "undo_stack": [state.get_state() for state in self.undo_stack],
                            "redo_stack": [state.get_state() for state in self.redo_stack]
                          }, 
                          file, indent=4)
        except FileNotFoundError:
            raise FileNotFoundError(f"File wasn't found at {self.file_path}")

    def save_state(self):
        self.undo_stack.append(self.current_memento)
        self.redo_stack.clear()
        self.current_memento = self.receiver.create_memento()
        self._save_data()

    def load_state(self):
        self._load_data()
        self.receiver.load_memento(self.current_memento)

    def undo(self):
        self._load_data()
        if not self.undo_stack: # Is undo_stack empty
            print("No states before was found")
            return
        self.redo_stack.append(self.current_memento)
        self.current_memento = self.undo_stack.pop()
        self.receiver.load_memento(self.current_memento)
        self._save_data()

    def redo(self):
        self._load_data()
        if not self.redo_stack: # Is redo_stack empty
            print("No states after was found")
            return
        self.undo_stack.append(self.current_memento)
        self.current_memento = self.redo_stack.pop()
        self.receiver.load_memento(self.current_memento)
        self._save_data()
