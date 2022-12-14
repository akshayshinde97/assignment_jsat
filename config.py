"""
Configuration file for the application.
"""
from datetime import timedelta
import os

basedir = os.path.abspath(os.path.dirname(
    __file__))  # pylint: disable=invalid-name


class Config(object):
    """
    Common configurations
    """
    # Put any configurations here that are common across all environments
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SECRET_KEY = os.environ['SECRET_KEY']
    DB_USERNAME = os.environ['MYSQL_USER']
    DB_PASSWORD = os.environ['MYSQL_PASSWORD']
    DB_HOST = os.environ['MYSQL_HOST']
    DATABASE_NAME = os.environ['MYSQL_DATABASE']
    DB_URI = "mysql://%s:%s@%s:3306/%s" % (DB_USERNAME,
                                           DB_PASSWORD, DB_HOST, DATABASE_NAME)
    MYSQL_ROOT_PASSWORD = os.environ['MYSQL_ROOT_PASSWORD']
    SQLALCHEMY_DATABASE_URI = DB_URI
    JWT_SECRET_KEY = 'jwt-secret-string'
    JWT_BLACKLIST_ENABLED: True
    PROPAGATE_EXCEPTIONS = True
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)


class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False


class StagingConfig(Config):
    """
    Staging configurations
    """
    DEBUG = True


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True


print(DevelopmentConfig.SQLALCHEMY_DATABASE_URI)
