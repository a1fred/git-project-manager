import webbrowser

from git_project.categories.abc import command
from ..db import wm


class Command(command.Command):
    command = 'open'
    help = ''

    def add_arguments(self, parser):
        parser.add_argument("title", type=str, nargs="+")

    def handle(self, **kwargs):
        titlestr = " ".join(kwargs['title'])
        article = wm.get_article(titlestr)
        if article:
            fpath = wm._getfpath(titlestr)
            webbrowser.open(fpath)
        else:
            print(f"Article {titlestr} not exists.")
