from dataclasses import dataclass


@dataclass
class Ticket:
    status: str
    title: str

    id: str = ''
    assignee: str = ''

    def __str__(self):
        return f"[{self.status.upper()}] {self.assignee} #{self.id}: {self.title}"
