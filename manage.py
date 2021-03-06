from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager

from ivadb.factory import create_app
from ivadb.core import db


app = create_app()
Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
