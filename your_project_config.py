from os import path, environ

# Wherever an encoding is needed, this configuration value is used.
ENCODING = 'utf8'

# Credentials of the root user. Will be created/updated automatically.
# There can only be one root user at a time.
ROOT_USER = {
  'name': 'root',
  'password': 'alpine',
  'email': 'admin@example.org',
}

# Deployment directory for data files.
DEPLOY_DIR = environ.get('CRAFTR_WEB_DEPLOY_DIR')
if not DEPLOY_DIR:
  DEPLOY_DIR = path.join(path.dirname(__file__), '_deploy_test')

# Database configuration. These parameters are passed directly to db.bind().
DB_PROVIDER = 'sqlite'
DB_CONFIG = {
  'filename': path.join(DEPLOY_DIR, 'test_db.sqlite'),
  'create_db': True,
}
