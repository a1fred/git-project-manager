from git_project.categories.abc import command
from ..db import get_wm


class Command(command.Command):
    command = 'list'
    help = ''

    def handle(self, **kwargs):
        wm = get_wm(self.settings)
        for title in wm.get_articles():
            print(f" * {title}")
