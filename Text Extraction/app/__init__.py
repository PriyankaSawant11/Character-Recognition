import flask

app = flask.Flask(__name__)

app.config.from_object("config.DevelopmentConfig")

from app import views
