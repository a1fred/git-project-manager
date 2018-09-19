from typing import List

from . import ticket, wiki
from .abc.category import Category


CATEGORIES: List[Category] = [
    ticket.Category(),
    wiki.Category(),
]
