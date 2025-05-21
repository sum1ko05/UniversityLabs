from virtual_keyboard import RealKeyboard
from virtual_receiver import VirtualReceiver
from memento import MemoryMementoManager
import commands
import keyboard

def dummy(event):
    pass

receiver = VirtualReceiver()
real_keyboard = RealKeyboard()
memento_manager = MemoryMementoManager(receiver)
real_keyboard.command = commands.KeyCommand(receiver)
'''real_keyboard.execute(key='o')
real_keyboard.execute(key='w')
real_keyboard.execute(key='s')
real_keyboard.execute(key='backspace')
real_keyboard.execute(key='o')'''

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
        memento_manager.load_state()
        keyboard.on_release(dummy)
        continue
    elif pressed_key == 'alt':
        memento_manager.save_state()
        keyboard.on_release(dummy)
        continue
    else:
        real_keyboard.command = commands.KeyCommand(receiver)
    real_keyboard.execute(key=pressed_key)
    keyboard.on_release(dummy)