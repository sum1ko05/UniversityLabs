from typing import Protocol
from virtual_receiver import VirtualReceiver
from memento import MementoManagerProtocol


class CommandProtocol(Protocol):
    def execute(self, **kwargs):
        ...


class KeyCommand(CommandProtocol):
    def __init__(self, executor: VirtualReceiver):
        self.__executor = executor

    def execute(self, **kwargs):
        self.__executor.press_key(key=kwargs['key'])


class VolumeUpCommand(CommandProtocol):
    def __init__(self, executor: VirtualReceiver):
        self.__executor = executor

    def execute(self, **kwargs):
        self.__executor.volume_up()


class VolumeDownCommand(CommandProtocol):
    def __init__(self, executor: VirtualReceiver):
        self.__executor = executor

    def execute(self, **kwargs):
        self.__executor.volume_down()


class MediaPlayerCommand(CommandProtocol):
    def __init__(self, executor: VirtualReceiver):
        self.__executor = executor

    def execute(self, **kwargs):
        self.__executor.media_player()


class SaveStateCommand(CommandProtocol):
    def __init__(self, executor: MementoManagerProtocol):
        self.__executor = executor

    def execute(self, **kwargs):
        self.__executor.save_state()


class LoadStateCommand(CommandProtocol):
    def __init__(self, executor: MementoManagerProtocol):
        self.__executor = executor

    def execute(self, **kwargs):
        self.__executor.load_state()
