from git_project.categories.abc import command
from git_project.utils.shortcuts import startfile
from git_project.utils.colors import C

from ..db import get_wm


class Command(command.Command):
    command = 'open'
    help = ''

    def add_arguments(self, parser):
        parser.add_argument("title", type=str, nargs="+")

    def handle(self, **kwargs):
        wm = get_wm(self.category.settings)

        titlestr = " ".join(kwargs['title'])
        article = wm.get_article(titlestr)
        if article:
            fpath = wm._getfpath(titlestr)
            print(f"{C.OKGREEN}Opening {C.OKBLUE}{C.BOLD}{titlestr}{C.ENDC}{C.OKGREEN}...{C.ENDC}")
            startfile(fpath)
        else:
            print(f"{C.WARNING}Article {C.OKBLUE}{C.BOLD}{titlestr}{C.ENDC}{C.WARNING} not exists.{C.ENDC}")
