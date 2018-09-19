from typing import Iterable, Optional
import configparser
from dataclasses import asdict

from git_project import constants
from .utils import ensure_dir_exists
from .models import Ticket


class DirDb:
    def __init__(self, dbpath: str, prefix="GT") -> None:
        ensure_dir_exists(dbpath)
        self.dbpath = dbpath
        self.prefix = prefix
        self.issuesfilepath = f"{dbpath}/{constants.ISSUES_FILE}"
        self.config = configparser.ConfigParser()
        self.config.read(self.issuesfilepath)

    def _savedb(self):
        with open(self.issuesfilepath, 'w') as configfile:
            self.config.write(configfile)

    def iterate(self) -> Iterable[Ticket]:
        for tid in self.config.sections():
            yield Ticket(id=tid, **self.config[tid])

    def insert_ticket(self, ticket: Ticket):
        assert ticket.id is ''

        def get_new_ticket_id() -> str:
            i = 1
            while True:
                newid = f"{self.prefix}{i}"
                if newid not in self.config.sections():
                    return f"{self.prefix}{i}"
                else:
                    i += 1
        ticket.id = get_new_ticket_id()

        return self.update_ticket(ticket)

    def update_ticket(self, ticket: Ticket):
        assert ticket.id

        ticketdict: dict = asdict(ticket)
        key = ticketdict.pop('id')
        self.config[key] = ticketdict
        self._savedb()
        return ticket

    def get_ticket_by_id(self, ticketid: str) -> Optional[Ticket]:
        for tid in self.config.sections():
            if ticketid == tid:
                return Ticket(id=tid, **self.config[tid])
        return None
