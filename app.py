"""
Command for running the application
"""

#  imports
import click
from flask_migrate import Migrate
from flask_cors import CORS

# local imports
from config import DevelopmentConfig
from store.db import db
from store import create_app
from store.db import *


app = create_app(DevelopmentConfig)

cors = CORS(app, resources={r"*": {"origins": "*"}})

migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run()
    # os.environ['FLASK_APP'] = __file__
    # app.cli()
