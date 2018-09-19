import os


def attrEqual(obj, name, value) -> bool:
    if not hasattr(obj, name):
        return False
    else:
        return getattr(obj, name) == value


def ensure_dir_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
