#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from flask import Flask
import controller
from extensions import db


DEFAULT_MODULES = (
    (controller.frontend, ""),
)

def create_app(modules=None):

    if modules is None:
        modules = DEFAULT_MODULES   
    
    app = Flask(__name__)
    
    # config
    app.config.from_object('flask_boilerplate.config.DevelopmentConfig')
    
    configure_extensions(app)

    configure_before_handlers(app)

    #configure_error_handler
    
    # register module
    configure_modules(app, modules) 

    return app

#configure_extensions
def configure_extensions(app):
    db.init_app(app)

def configure_before_handlers(app):
    @app.before_request
    def init_table():
        db.create_all()

#configure_modules
def configure_modules(app, modules):
    for module, url_prefix in modules:
        app.register_module(module, url_prefix=url_prefix)
