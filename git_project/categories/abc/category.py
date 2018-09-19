from typing import List
from .command import Command


class Category:
    name: str
    help: str
    commands: List[Command]

    def handle_command(self, command: str, **kwargs):
        for c in self.commands:
            if c.command == command:
                return c.handle(**kwargs)

        raise ValueError(command, **kwargs)
