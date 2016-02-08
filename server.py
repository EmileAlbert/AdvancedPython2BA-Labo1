# server.py
# Math tools web application
# Author: Sébastien Combéfis
# Version: February 3, 2016

import os
from bottle import route, run, template, error, post, request, static_file
import utils

@route('/')
def home():
    return 'Hello World!'

@route('/hello/<name>')
def hello(name):
    return 'Hello {}'.format(name)

@route('/sum/<a>/<b>')
def sum(a,b):
    print(type(a))
    sum = int(a) + int(b)
    return template('{{a}} + {{b}} = {{s}}', a =a, b=b, s = sum)

@route('/fact/<n>')
def fact(n) :
    var = int(n)
    result = utils.fact(var)
    return template('La factorielle de {{a}} est {{b}}', a=n,b=result)


run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

