from ..abc import category, settings, command

"""
Webui module
"""


class ServeCommand(command.Command):
    command = 'serve'
    help = 'Start webui'

    def add_arguments(self, parser):
        parser.add_argument("-a", "--address", type=str, default="localhost")
        parser.add_argument("-p", "--port", type=int, default=8080)

    def handle(self, **kwargs):
        from .webapp import app
        return app.run(host=kwargs['address'], port=kwargs['port'], debug=True)


class CategorySettings(settings.Settings):
    pass


class Category(category.Category):
    name = 'webui'
    help = 'WebUI'
    settings = CategorySettings()

    def get_commands(self):
        return [
            ServeCommand(self),
        ]
