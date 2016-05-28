import os
import flask
from . import config

app = flask.Flask(__name__.split('.')[0])

from . import models, views

def run(*args, **kwargs):
  if not os.path.exists(config.DEPLOY_DIR):
    os.makedirs(config.DEPLOY_DIR)
  models.db.bind(config.DB_PROVIDER, **config.DB_CONFIG)
  models.db.generate_mapping(create_tables=True)
  return app.run(*args, **kwargs)
