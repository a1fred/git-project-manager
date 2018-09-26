from typing import List
from .command import Command


class Category:
    name: str
    help: str
    commands: List[Command]

    def __init__(self) -> None:
        self.commands = self.get_commands()

    def get_commands(self) -> List[Command]:
        raise NotImplementedError

    def handle_command(self, command: str, **kwargs):
        for c in self.commands:
            if c.command == command:
                return c.handle(**kwargs)

        raise ValueError(command, **kwargs)
