import flask
from . import config

app = flask.Flask(__name__.split('.')[0])

from . import models, views

def run(*args, **kwargs):
  return app.run(*args, **kwargs)
