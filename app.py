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
import logging
from logging.config import dictConfig

logging_schema = {
    "version": 1,
    'disable_existing_loggers': False,
    "formatters": {
        # Formatter Name
        "standard": {
            # class is always "logging.Formatter"
            "class": "logging.Formatter",
            # Optional: logging output format
            "format": "%(asctime)s\t%(levelname)s\t%(filename)s\t%(message)s",
            # Optional: asctime format
            "datefmt": "%d %b %y %H:%M:%S"
        }
    },
    # Handlers use the formatter names declared above
    "handlers": {
        # Name of handler
        "console": {
            # The class of logger. A mixture of logging.config.dictConfig() and
            # logger class-specific keyword arguments (kwargs) are passed in here.
            "class": "logging.StreamHandler",
            # This is the formatter name declared above
            "formatter": "standard",
            "level": "DEBUG",
            # The default is stderr
            "stream": "ext://sys.stdout"
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "standard",
            "level": "DEBUG",
            "filename": "store_app_logs.log",
            "mode": "a",
            "encoding": "utf-8",
            "maxBytes": 500000,
            "backupCount": 4
        }
    },
    # Loggers use the handler names declared above
    "loggers": {
        "store_app": {
            # Use a list even if one handler is used
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": False
        }
    },
    # Just a standalone kwarg for the root logger
    "root": {
        "level": "DEBUG",
        "handlers": ["file"]
    }
}

app = create_app(DevelopmentConfig)
dictConfig(logging_schema)

cors = CORS(app, resources={r"*": {"origins": "*"}})

migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run()
    # os.environ['FLASK_APP'] = __file__
    # app.cli()
