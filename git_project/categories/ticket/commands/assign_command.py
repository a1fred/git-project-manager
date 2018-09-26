from git_project.categories.abc import command
from ..db import get_tm
from git_project.utils.githelpers import get_git_user


class Command(command.Command):
    command = 'assign'
    help = 'Assign to me'

    def add_arguments(self, parser):
        parser.add_argument("tid", type=str)

    def handle(self, **kwargs):
        tm = get_tm(self.category.settings)
        tid = kwargs['tid']

        ticket = tm.get_ticket_by_id(tid)
        if ticket:
            my_user = get_git_user()
            print(my_user)
            t = tm.update(ticket, assignee=my_user)
            print(t)
        else:
            print(f"Ticket {tid} not found")
