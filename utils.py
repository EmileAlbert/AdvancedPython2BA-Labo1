from math import *

# Math library
# Author: Sébastien Combéfis
# Version: February 2, 2016


def fact(n):
    """Computes the factorial of a natural number.
    
    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """
    if n<2:
        return 1
    else:
        return n*fact(n-1)


def roots(a, b, c):
    """Computes the roots of the ax^2 + bx + x = 0 polynomial.
    
    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
          to the roots of the ax^2 + bx + c polynomial.
    """
    delta = (b*b)-(4*a*c)
    if delta < 0 :
        return None
    elif delta == 0 :
        return -b/2*a
    elif delta > 0 :
        return (-b+sqrt(delta))/2*a, (-b-sqrt(delta))/2*a


'''def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """'''




if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 0,1 ))
    #print(integrate('x ** 2 - 1', -1, 1))