from dataclasses import dataclass

from git_project.utils.colors import C


@dataclass
class Ticket:
    status: str
    title: str

    id: str = ''
    assignee: str = ''

    def __str__(self):
        fields = [
            f"{C.HEADER}[{self.status.upper()}]{C.ENDC}",
            f"{C.WARNING}#{self.id}{C.ENDC}",
        ]

        if self.assignee:
            fields.append(f"{C.OKGREEN}[{self.assignee}]{C.ENDC}:")
        else:
            fields.append("\b:")

        fields.append(f"{self.title}")

        return " ".join(fields)
