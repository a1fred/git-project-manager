from typing import Iterable, Optional

from .models import Ticket
from .utils import attrEqual
from .db import DirDb
from git_project import constants


__all__ = ['tm', 'models']


class TicketsManager:
    def __init__(self, dbpath: str) -> None:
        self.db = DirDb(dbpath)

    def add(self, title: str, status="open") -> Ticket:
        ticket = self.db.insert_ticket(
            Ticket(title=title, status=status)
        )
        assert ticket.id
        return ticket

    def find(self, **kwargs) -> Iterable[Ticket]:
        for ticket in self.db.iterate():
            if all([attrEqual(ticket, name, value) for name, value in kwargs.items()]):
                yield ticket

    def get_ticket_by_id(self, tid: str) -> Optional[Ticket]:
        return self.db.get_ticket_by_id(tid)

    def update(self, ticket: Ticket, **kwargs):
        for k, v in kwargs.items():
            setattr(ticket, k, v)
            self.db.update_ticket(ticket)
        return ticket


tm = TicketsManager(constants.PROJECT_DIR)
