from flask.views import MethodView
from flask import render_template


class IndexView(MethodView):
    def get(self):
        return render_template('index.jinja2')


class AboutView(MethodView):
    def get(self):
        return render_template('about.jinja2')
