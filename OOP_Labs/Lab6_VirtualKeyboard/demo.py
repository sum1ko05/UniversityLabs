from invokers import RealKeyboard
from virtual_receiver import SaveableTyper, SaveableMediaPlayer
from memento import MemoryMementoManager, JSONMementoManager
from originator import CompositeOriginator
import commands
import keyboard
from enum import Enum


class Keys(Enum):
    Volume_down = 'f3'
    Volume_up = 'f4'


def dummy(event):
    pass


composite_receiver = CompositeOriginator()
composite_receiver.add_component(SaveableTyper(), "typer")
composite_receiver.add_component(SaveableMediaPlayer(), "player")
#receiver = VirtualReceiverLegacy()
real_keyboard = RealKeyboard()
memento_manager = JSONMementoManager(composite_receiver, file_path="saves/memento.json")
real_keyboard.command = commands.KeyCommand(composite_receiver)

real_keyboard.command = commands.LoadStateCommand(memento_manager)
real_keyboard.execute()

while True:
    pressed_key = keyboard.read_key()
    if pressed_key == 'up':
        real_keyboard.command = commands.VolumeUpCommand(composite_receiver.get_component("player"))
    elif pressed_key == 'down':
        real_keyboard.command = commands.VolumeDownCommand(composite_receiver.get_component("player"))
    elif pressed_key == 'f7':
        real_keyboard.command = commands.MediaPlayerCommand(composite_receiver.get_component("player"))
    elif pressed_key == 'esc':
        break
    elif pressed_key == 'left':
        real_keyboard.command = commands.UndoCommand(memento_manager)
    elif pressed_key == 'right':
        real_keyboard.command = commands.RedoCommand(memento_manager)
    else:
        real_keyboard.command = commands.KeyCommand(composite_receiver.get_component("typer"))
    real_keyboard.execute(key=pressed_key)
    if (type(real_keyboard.command) != type(commands.UndoCommand(memento_manager)) and 
        type(real_keyboard.command) != type(commands.RedoCommand(memento_manager))):
        real_keyboard.command = commands.SaveStateCommand(memento_manager)
        real_keyboard.execute()
    #print(pressed_key)
    keyboard.on_release(dummy)
#sop