from ..abc import category, settings
from .commands import (
    list_command,
    add_command,
    close_command,
    assign_command,
)

"""
Ticket management module
"""


class CategorySettings(settings.Settings):
    ticket_prefix = "GT"
    issues_file = "issues.ini"

    default_status = 'open'
    additional_statuses = [
        'wip'
        'testing',
    ]
    status_closed = 'closed'

    @property
    def statuses_workflow(self):
        return [self.default_status, ] + self.additional_statuses

    @property
    def all_statuses(self):
        return self.statuses_workflow + [self.status_closed, ]


class Category(category.Category):
    name = 'ticket'
    help = 'Tickets manager'
    settings = CategorySettings()

    def get_commands(self):
        return [
            list_command.Command(self),
            add_command.Command(self),
            close_command.Command(self),
            assign_command.Command(self),
        ]
