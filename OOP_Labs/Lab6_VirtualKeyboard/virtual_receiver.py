from neat_console.printer_base import Color, Printer
from typing import Protocol
import os
clear = lambda: os.system('cls')


class SaveableMemento:
    def __init__(self, properties: dict):
        self.prop_state = properties

    def get_state(self) -> dict:
        return self.prop_state
    
    def __str__(self):
        return self.prop_state
    

class SaveableProtocol(Protocol):
    def create_memento(self):
        ...

    def load_memento(self, memento: SaveableMemento):
        ...


class SaveableTyper(SaveableProtocol):
    def __init__(self):
        self.__string = ""
        self.neat_console = Printer(color=Color.LightWhite,
                                    position=(0, 0),
                                    font_path="neat_console/default.json")

    def press_key(self, key: str):
        clear()
        if key == 'backspace' and len(self.__string) > 0:
            self.__string = self.__string[:-1]
        elif key == 'space':
            self.__string = self.__string + " "
        elif key.isalpha() and len(key) == 1:
            self.__string = self.__string + key
        self.neat_console.print(self.__string)

    def create_memento(self) -> SaveableMemento:
        print("Typer memento saved")
        return SaveableMemento({'string': self.__string})

    def load_memento(self, memento: SaveableMemento):
        state = memento.get_state()
        self.__string = state['string']

        print("Typer memento loaded")
        self.neat_console.print(self.__string)


class SaveableMediaPlayer(SaveableProtocol):
    def __init__(self):
        self.__volume = 50
        self.media_player_state = False

    def volume_up(self):
        self.__volume = min(self.__volume + 10, 100)
        print(f"Volume: {self.__volume}")

    def volume_down(self):
        self.__volume = max(self.__volume - 10, 0)
        print(f"Volume: {self.__volume}")

    def media_player(self):
        self.media_player_state = not self.media_player_state
        if self.media_player_state:
            print("Media player ON")
        else:
            print("Media player OFF")

    def create_memento(self) -> SaveableMemento:
        print("Player memento saved")
        return SaveableMemento({'volume': self.__volume,
                                'media': self.media_player_state})

    def load_memento(self, memento: SaveableMemento):
        state = memento.get_state()
        self.__volume = state['volume']
        self.media_player_state = state['media']

        print("Player memento loaded")
        print(f"Volume: {self.__volume}")
        print(f"Media player {"ON" if self.media_player_state == True else "OFF"}")

