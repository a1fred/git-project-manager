from git_project.categories.abc import command
from ..db import get_wm


class Command(command.Command):
    command = 'create'
    help = ''

    def add_arguments(self, parser):
        parser.add_argument("title", type=str, nargs="+")

    def handle(self, **kwargs):
        wm = get_wm(self.category.settings)

        titlestr = " ".join(kwargs['title'])
        article = wm.get_article(titlestr)
        if article:
            print(f"Article {titlestr} already exists.")
        else:
            wm.create_article(titlestr)
            print(f"Empty article {titlestr} created.")
