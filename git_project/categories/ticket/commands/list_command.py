from git_project.categories.abc import command
from ..db import tm


class Command(command.Command):
    command = 'list'
    help = ''

    def add_arguments(self, parser):
        parser.add_argument("-s", "--status", type=str, default="open")

    def handle(self, **kwargs):
        print("List:")
        for t in tm.find(status=kwargs['status']):
            print(f" - {t}")
