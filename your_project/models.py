from pony import orm
from pony.orm import db_session
from . import config

db = orm.Database()

## Entity declarations

db.bind(config.db_kind, **config.db_config[config.db_kind])
db.generate_mapping(create_tables=True)
