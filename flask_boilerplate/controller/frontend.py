#! /usr/bin/env python
#coding=utf-8

import datetime
import os

from flask import Module, Response, request, flash, jsonify, g, current_app,\
    abort, redirect, url_for, session, send_file, send_from_directory
from flask import render_template

from flask_boilerplate.extensions import db
from flask_boilerplate.models import User

frontend = Module(__name__)

@frontend.route('/')
def main():
    return render_template('index.html')

