from ..abc import category
from .commands import (
    list_command,
    create_command,
    open_command,
    echo_command,
)

"""
Wiki module
"""


class Category(category.Category):
    name = 'wiki'
    help = 'Wiki manager'

    commands = [
        list_command.Command(),
        create_command.Command(),
        open_command.Command(),
        echo_command.Command(),
    ]
