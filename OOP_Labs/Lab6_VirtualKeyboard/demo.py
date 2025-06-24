from invokers import RealKeyboard, KeybindCommandConnector
from virtual_receiver import SaveableTyper, SaveableMediaPlayer
from memento import MemoryMementoManager, JSONMementoManager
from originator import CompositeOriginator
import commands
import keyboard
from enum import Enum


class Keys(Enum):
    Volume_down = 'down'
    Volume_up = 'up'
    Media = 'f7'
    Undo_action = 'left'
    Redo_action = 'right'
    # Virtual keys for technical commands, no activation from keyboard
    Load_state = 'technical_load'
    Save_state = 'technical_save'


def dummy(event):
    pass


composite_receiver = CompositeOriginator()
composite_receiver.add_component(SaveableTyper(), "typer")
composite_receiver.add_component(SaveableMediaPlayer(), "player")
#receiver = VirtualReceiverLegacy()
#real_keyboard = RealKeyboard()
memento_manager = JSONMementoManager(composite_receiver, file_path="saves/memento.json")
#
commander = KeybindCommandConnector()
commander.default_command = commands.KeyCommand(composite_receiver.get_component("typer"))

commander.add_command(commands.VolumeUpCommand(composite_receiver.get_component("player")), keybind=Keys.Volume_up.value)
commander.add_command(commands.VolumeDownCommand(composite_receiver.get_component("player")), keybind=Keys.Volume_down.value)
commander.add_command(commands.MediaPlayerCommand(composite_receiver.get_component("player")), keybind=Keys.Media.value)

commander.add_command(commands.UndoCommand(memento_manager), keybind=Keys.Undo_action.value)
commander.add_command(commands.RedoCommand(memento_manager), keybind=Keys.Redo_action.value)
# Again, technical commands, no activation from keyboard
commander.add_command(commands.LoadStateCommand(memento_manager), keybind=Keys.Load_state.value)
commander.add_command(commands.SaveStateCommand(memento_manager), keybind=Keys.Save_state.value)

commander.execute(Keys.Load_state.value) # Preloading state
while True:
    pressed_key = keyboard.read_key()
    if pressed_key == 'esc':  # It should let us exit the program
        break
    else:  # Any functional keys
        commander.execute(pressed_key, key=pressed_key)
        # Condition for preventing history corruption
        if (pressed_key != Keys.Undo_action.value) and (pressed_key != Keys.Redo_action.value):
            commander.execute(Keys.Save_state.value)
    keyboard.on_release(dummy)  # Just for comfortable typing
