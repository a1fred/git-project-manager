from git_project.categories.abc import command
from git_project.utils.colors import C

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
                if ticket.status != self.category.settings.status_closed:
                    t = tm.update(ticket, status=self.category.settings.status_closed)
                    updated.append(t)
                else:
                    print(f"{C.FAIL}Ticket {C.WARNING}#{tid}{C.ENDC}{C.FAIL} already closed{C.ENDC}")
            else:
                print(f"{C.FAIL}Ticket {C.WARNING}#{tid}{C.ENDC}{C.FAIL} not found{C.ENDC}")

        if updated:
            print(f"{C.OKBLUE}Ticket updated:{C.ENDC}")
            for t in updated:
                print(f" - {t}")
