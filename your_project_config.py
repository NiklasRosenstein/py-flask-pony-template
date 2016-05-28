import os

deploy_dir = os.getenv('CRAFTR_FARM_DEPLOYMENT_DIR', '')
if not deploy_dir:
  deploy_dir = os.path.join(os.path.dirname(__file__), '.devdeploy')
if not os.path.isdir(deploy_dir):
  os.makedirs(deploy_dir)

db_kind = 'sqlite'
db_config = {
  'sqlite': {
    'filename': os.path.join(deploy_dir, 'test_db.sqlite'),
    'create_db': True,
  },
}
