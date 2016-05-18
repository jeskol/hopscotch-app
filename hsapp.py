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
        for filename in ['bands.sql', 'users.sql', 'ratings.sql']:
            with app.open_resource(filename, mode='r') as f:
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
    g.cursor = g.db.cursor()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/', methods=['GET', 'POST'])
def test():
    g.cursor.execute('select * from tester')
    output = {'data': []}
    for rId, name, addr in g.cursor:
        output['data'].append({'id': rId, 'name': name, 'address': addr})
    return render_template('test.html', output=output)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
