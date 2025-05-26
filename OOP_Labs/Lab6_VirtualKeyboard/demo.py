from invokers import RealKeyboard
from virtual_receiver import VirtualReceiver
from memento import MemoryMementoManager, JSONMementoManager
import commands
import keyboard
from enum import Enum


class Keys(Enum):
    Volume_down = 'f3'
    Volume_up = 'f4'


def dummy(event):
    pass


receiver = VirtualReceiver()
real_keyboard = RealKeyboard()
memento_manager = JSONMementoManager(receiver, file_path="saves/memento.json")
real_keyboard.command = commands.KeyCommand(receiver)

while True:
    pressed_key = keyboard.read_key()
    if pressed_key == 'f3':
        real_keyboard.command = commands.VolumeUpCommand(receiver)
    elif pressed_key == 'f2':
        real_keyboard.command = commands.VolumeDownCommand(receiver)
    elif pressed_key == 'f7':
        real_keyboard.command = commands.MediaPlayerCommand(receiver)
    elif pressed_key == 'esc':
        break
    elif pressed_key == 'ctrl':
        real_keyboard.command = commands.LoadStateCommand(memento_manager)
    elif pressed_key == 'alt':
        real_keyboard.command = commands.SaveStateCommand(memento_manager)
    else:
        real_keyboard.command = commands.KeyCommand(receiver)
    real_keyboard.execute(key=pressed_key)
    keyboard.on_release(dummy)
#