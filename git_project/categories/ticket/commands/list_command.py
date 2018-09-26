from git_project.categories.abc import command
from ..db import get_tm


class Command(command.Command):
    command = 'list'
    help = 'Show issues list'

    def add_arguments(self, parser):
        parser.add_argument(
            "-s", "--status", type=str,
            default=self.category.settings.default_status,
            choices=['all', ] + self.category.settings.all_statuses
        )

    def handle(self, **kwargs):
        print("List:")
        tm = get_tm(self.category.settings)

        if kwargs['status'] == 'all':
            for t in tm.find():
                print(f" - {t}")
        else:
            for t in tm.find(status=kwargs['status']):
                print(f" - {t}")
