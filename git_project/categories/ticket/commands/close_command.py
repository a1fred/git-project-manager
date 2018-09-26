from git_project.categories.abc import command
from ..db import get_tm


class Command(command.Command):
    command = 'close'
    help = ''

    def add_arguments(self, parser):
        parser.add_argument("tids", type=str, nargs="+")

    def handle(self, **kwargs):
        tm = get_tm(self.category.settings)
        updated = []

        for tid in kwargs['tids']:
            ticket = tm.get_ticket_by_id(tid)
            if ticket:
                if ticket.status != self.category.status_closed:
                    t = tm.update(ticket, status=self.category.status_closed)
                    updated.append(t)
                else:
                    print(f"Ticket {tid} already closed")
            else:
                print(f"Ticket {tid} not found")

        if updated:
            print("Ticket updated:")
            for t in updated:
                print(f" - {t}")
