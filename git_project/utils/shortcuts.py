import os
import platform
from subprocess import check_output
from typing import List


def attrEqual(obj, name, value) -> bool:
    if not hasattr(obj, name):
        return False
    else:
        return getattr(obj, name) == value


def ensure_dir_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def run_shell(cmd: List[str]) -> str:
    return check_output(cmd, timeout=30).decode("utf-8").strip()


def startfile(fpath: str) -> None:
    os_famity = platform.system() 
    if os_famity == 'Linux':
        os.system(f"xdg-open {fpath}")
    elif os_famity == "Darwin":
        os.system(f"open {fpath}")
    elif os_famity == "Windows":
        os.startfile(fpath)
    else:
        raise NotImplementedError(f"Unsuported OS: {os_famity}")
