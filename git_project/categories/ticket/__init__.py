from ..abc import category
from .commands import (
    list_command,
    add_command,
    close_command,
)

"""
Ticket management module
"""


class Category(category.Category):
    name = 'ticket'
    help = 'Tickets manager'

    commands = [
        list_command.Command(),
        add_command.Command(),
        close_command.Command(),
    ]
