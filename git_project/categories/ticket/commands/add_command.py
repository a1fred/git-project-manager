from git_project.categories.abc import command
from git_project.utils.colors import C
from git_project.utils.githelpers import get_git_user

from ..db import get_tm


class Command(command.Command):
    command = 'add'
    help = 'Add issue'

    def add_arguments(self, parser):
        parser.add_argument("title", type=str, nargs="+")
        parser.add_argument("-a", "--assign", action='store_true', default=False)
        parser.add_argument(
            "-s", "--status", type=str,
            default=self.category.settings.default_status,
            choices=self.category.settings.all_statuses,
        )

    def handle(self, **kwargs):
        tm = get_tm(self.category.settings)

        titlestr = " ".join(kwargs['title'])
        assignee = ''
        if kwargs['assign'] is True:
            assignee = get_git_user()

        t = tm.add(title=titlestr, assignee=assignee, status=kwargs['status'])
        print(f"{C.OKBLUE}New ticket added:{C.ENDC}")
        print(f" - {t}")
