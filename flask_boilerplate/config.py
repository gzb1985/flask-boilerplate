#!/usr/bin/env python

# http://flask.pocoo.org/docs/config/#development-production

class Config(object):
    SITE_NAME = 'flask_boilerplate'
    SECRET_KEY = "your app secret key"
    MEMCACHED_SERVERS = ['localhost:11211']
    SYS_ADMINS = ['gzb1985@gmail.com']

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

class TestConfig(Config):
    DEBUG = False
    TESTING = True

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_ECHO = False

