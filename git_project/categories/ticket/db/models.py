from dataclasses import dataclass


@dataclass
class Ticket:
    status: str
    title: str

    id: str = ''
    assignee: str = ''

    def __str__(self):
        if self.assignee:
            return f"[{self.status.upper()}] #{self.id} [{self.assignee}]: {self.title}"
        else:
            return f"[{self.status.upper()}] #{self.id}: {self.title}"
