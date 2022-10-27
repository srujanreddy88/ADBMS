from bottle import default_app, route, get, post, template, request, redirect
import sqlite3



@route('/')
def hello_world():
    return 'Hello world!'

@route('/hi')
def hi_world():
    return 'Hi from srujan'

@route('/bye')
def bye_world():
    return 'Bye from srujan'

application = default_app()