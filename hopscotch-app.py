#! /usr/bin/env python

from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import mysql.connector as mariadb

# default configuration
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
DBUSER = 'root'
DBPASS = 'hopscotch'
DBHOST = '127.0.0.1'
DATABASE = 'test'

# create app
app = Flask(__name__)
app.config.from_object(__name__)

app.config.from_envvar('HSAPP_SETTINGS', silent=False)

# This may not work with mysql
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().execute(f.read())
        db.commit()

def connect_db():
    return mariadb.connect(
        user=app.config['DBUSER'],
        password=app.config['DBPASS'],
        host=app.config['DBHOST'],
        database=app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

