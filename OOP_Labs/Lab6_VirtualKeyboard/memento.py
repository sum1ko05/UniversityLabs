from virtual_receiver import VirtualReceiver
from typing import Protocol

class MementoManagerProtocol(Protocol):
    def save_state():
        ...

    def load_state():
        ...

class MemoryMementoManager(MementoManagerProtocol):
    def __init__(self, receiver: VirtualReceiver):
        self.receiver = receiver
        self.memento = None

    def save_state(self):
        self.memento = self.receiver.create_memento()

    def load_state(self):
        if self.memento == None:
            print("Save slot is empty!")
        else:
            self.receiver.load_memento(self.memento)

class JSONMementoManager(MementoManagerProtocol):
    def __init__(self, receiver: VirtualReceiver):
        self.receiver = receiver
        self.memento = None

    def save_state(self):
        self.memento = self.receiver.create_memento()

    def load_state(self):
        if self.memento == None:
            print("Save slot is empty!")
        else:
            self.receiver.load_memento(self.memento)
