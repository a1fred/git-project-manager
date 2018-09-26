from .shortcuts import run_shell


def get_git_user() -> str:
    username = run_shell([
        'git',
        'config',
        'user.name',
    ])

    email = run_shell([
        'git',
        'config',
        'user.email',
    ])

    return f"{username} <{email}>"
