from typing import Optional, Tuple, List
import os

from git_project import constants
from git_project.categories.ticket.db.utils import ensure_dir_exists


class WikiManager:
    def __init__(self):
        self.wiki_path = f"{constants.PROJECT_DIR}/{constants.WIKI_DIR}"
        ensure_dir_exists(self.wiki_path)

    def _getfpath(self, title: str) -> str:
        return f"{self.wiki_path}/{title}.md"

    def get_article(self, title: str) -> Optional[Tuple[str, str]]:
        try:
            with open(self._getfpath(title), 'r+') as fp:
                contents = fp.read()
                return title, contents
        except IOError:
            return None

    def create_article(self, title: str) -> None:
        with open(self._getfpath(title), 'a'):
            pass

    def get_articles(self) -> List[str]:
        res = []
        for f in os.listdir(self.wiki_path):
            res.append(f[:-3])
        return res


wm = WikiManager()
