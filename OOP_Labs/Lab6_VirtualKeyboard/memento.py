from virtual_receiver import VirtualReceiver
from typing import Protocol
import json
from virtual_receiver import ReceiverMemento


class MementoManagerProtocol(Protocol):
    def save_state(self):
        ...

    def load_state(self):
        ...


class MemoryMementoManager(MementoManagerProtocol):
    def __init__(self, receiver: VirtualReceiver):
        self.receiver = receiver
        self.memento = None

    def save_state(self):
        self.memento = self.receiver.create_memento()

    def load_state(self):
        if self.memento is None:
            print("Save slot is empty!")
        else:
            self.receiver.load_memento(self.memento)


class JSONMementoManager(MementoManagerProtocol):
    def __init__(self, receiver: VirtualReceiver, file_path: str):
        self.receiver = receiver
        self.memento = None
        self.file_path = file_path

    def save_state(self):
        # self.memento = self.receiver.create_memento()
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.receiver.create_memento().prop_state, file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File wasn't found at {self.file_path}")

    def load_state(self):
        try:
            with open(self.file_path, 'r') as f:
                memento_dict = json.load(f)
                self.receiver.load_memento(ReceiverMemento(memento_dict))
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            print("Save slot is empty or wasn't found!")  # No memento found
