# -*- coding: utf-8 -*- 

from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, Response
from util import deployed_on_sae


app = Flask(__name__)

@app.route('/')
def main():
	return render_template('index.html')


from private_const import app_secret_key
app.debug = True
app.secret_key = app_secret_key


if __name__ == '__main__':
    app.run()