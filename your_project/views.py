from .app import app
from .models import db_session # .. and models

@app.route('/')
def index():
  return 'Hello, World!'
