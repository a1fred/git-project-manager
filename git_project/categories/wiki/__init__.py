from ..abc import category, settings
from .commands import (
    list_command,
    create_command,
    open_command,
    echo_command,
)

"""
Wiki module
"""


class CategorySettings(settings.Settings):
    workdir = 'wiki'


class Category(category.Category):
    name = 'wiki'
    help = 'Wiki manager'
    settings = CategorySettings()

    def get_commands(self):
        return [
            list_command.Command(self),
            create_command.Command(self),
            open_command.Command(self),
            echo_command.Command(self),
        ]
