from typing import List

from . import ticket, wiki, webui
from .abc.category import Category

category_classes = [ticket.Category, wiki.Category, webui.Category]
CATEGORIES: List[Category] = [x() for x in category_classes if x.supported()]
