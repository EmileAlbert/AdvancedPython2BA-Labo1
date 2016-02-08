# server.py
# Math tools web application
# Author: Sébastien Combéfis
# Version: February 3, 2016

import os
from bottle import route, run, template, error, post, request, static_file
import utils

@route('/')
def home():
    return '''
            Hello World! This Website <b>run on</b> !
            <br>With this app you can
            <ul>
                <li> Sum two numbers with <b>/sum/number1/number2</b></li>
                <li> Calculate factorial of a number with <b>/fact/number</b></li>
                <li> Computes the roots of the ax^2 + bx + x = 0 polynomial with <b>/roots/a/b/c</b></li>
            </ul>
            And maybe many more soon !
            '''

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

@route('/roots/<a>/<b>/<c>')
def roots(a,b,c) :
    result = utils.roots(int(a),int(b),int(c))
    if result == None :
        return "Il n'y a pas de racines réelles pour ce polynomes"
    else :
        return template('La ou les racines de {{a}}x² + {{b}}x + {{c}} = 0 est/sont {{res}}', a=a, b=b,c=c,res=result)


run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

