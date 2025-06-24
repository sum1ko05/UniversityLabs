import commands


# Invoker
class RealKeyboard:
    def __init__(self, init_command: commands.CommandProtocol | None = None):
        self._command = init_command

    @property
    def command(self):
        return self._command
    
    @command.setter
    def command(self, new_command: commands.CommandProtocol):
        self._command = new_command

    def execute(self, **kwargs):
        self.command.execute(**kwargs)


class KeybindCommandConnector:
    def __init__(self):
        self._invoker = RealKeyboard()
        self._keybinds = dict()

    @property
    def default_command(self):
        return self._default_command
    
    @default_command.setter
    def default_command(self, new_default_command: commands.CommandProtocol):
        self._default_command = new_default_command

    # region CRUD
    def add_command(self, command: commands.CommandProtocol, keybind: str):
        self._keybinds[keybind] = command

    def get_command(self, keybind: str):
        if keybind in self._keybinds.keys():
            return self._keybinds[keybind]
        else:
            return None
    
    def update_command(self, new_command: commands.CommandProtocol, keybind: str):
        if keybind in self._keybinds.keys():
            self._keybinds[keybind] = new_command

    def delete_command(self, keybind: str):
        self._keybinds.pop(keybind)
    # endregion

    def execute(self, keybind: str, **kwargs):
        command = self.get_command(keybind)
        if command is None:
            command = self.default_command
            if command is None:
                return
        # Command is set at this point
        self._invoker.command = command
        self._invoker.execute(**kwargs)
