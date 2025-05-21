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