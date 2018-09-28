import os

try:
    from flask import Flask
    from flask import render_template
except ImportError:
    Flask = None

from .controllers import (
    main,
)


if Flask is None:
    raise ImportError("You need install gitpm[webui] to use this module.")

TEMPLATES = 'templates'
STATIC = 'static'

basepath = os.path.dirname(__file__)

app = Flask(
    __name__,
    static_folder=os.path.join(basepath, STATIC),
    template_folder=os.path.join(basepath, TEMPLATES),
)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.jinja2'), 404


app.add_url_rule('/', view_func=main.IndexView.as_view('index'))
app.add_url_rule('/about', view_func=main.AboutView.as_view('about'))
