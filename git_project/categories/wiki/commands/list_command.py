from git_project.categories.abc import command
from ..db import wm


class Command(command.Command):
    command = 'list'
    help = ''

    def handle(self, **kwargs):
        for title in wm.get_articles():
            print(f" * {title}")
