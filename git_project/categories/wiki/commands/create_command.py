from git_project.categories.abc import command
from ..db import wm


class Command(command.Command):
    command = 'create'
    help = ''

    def add_arguments(self, parser):
        parser.add_argument("title", type=str, nargs="+")

    def handle(self, **kwargs):
        titlestr = " ".join(kwargs['title'])
        article = wm.get_article(titlestr)
        if article:
            print(f"Article {titlestr} already exists.")
        else:
            wm.create_article(titlestr)
            print(f"Empty article {titlestr} created.")
