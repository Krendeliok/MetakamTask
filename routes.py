from flask import Flask

from views.api import api_blueprint
from views.client import client_blueprint


def route(app: Flask):
    app.register_blueprint(api_blueprint)
    app.register_blueprint(client_blueprint)
