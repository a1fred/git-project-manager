from git_project.categories.abc import command
from ..db import tm


class Command(command.Command):
    command = 'add'
    help = ''

    def add_arguments(self, parser):
        parser.add_argument("title", type=str, nargs="+")

    def handle(self, **kwargs):
        titlestr = " ".join(kwargs['title'])
        t = tm.add(title=titlestr)
        print("New ticket added:")
        print(f" - {t}")
