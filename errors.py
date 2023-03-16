from function import func, der_func
from lagrangePolinomyal import sigmaSum
from scipy.misc import derivative
from math import factorial

def calculateAbsoluteError(n, values_x, values_y, x_star):
    f = func(x_star)
    sigma = sigmaSum(n, values_x, values_y, x_star)
    absoluteError = abs(sigma - f)
    return absoluteError

def calculateRelativeError(absolute_error, x_star):
    f = func(x_star)
    relativeError = absolute_error / abs(f)
    return relativeError

def calculateTheoryError(n, x_star, a, b):
    der = derivative(der_func, x_star, n=n, order=n+2)
    fact = factorial(n + 1)
    theoryError = (abs(der)/fact) * ((b - a)**(n + 1))
    return theoryError