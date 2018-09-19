class Command:
    command: str
    help: str

    def add_arguments(self, parser):
        pass

    def __init__(self):
        pass

    def handle(self, **kwargs):
        raise NotImplementedError
