from store.db import db
from flask import Flask
from store.models import *
from store import api


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(test_config)

    # # initialize the debug tool bar
    # debug_toolbar.init_app(app)

    # initialize SQLAlchemy
    db.init_app(app)
    api.init_api(app)

    @app.route('/hello')
    def hello():

        return 'Hello, World!'

    return app