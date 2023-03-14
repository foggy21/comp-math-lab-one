from lagrangePolinomyal import SigmaSum
from numpy import linspace
from math import log

# function x^2 + ln(x);
# [a; b] = [0,4; 0,9]
# x* = 0,52
# x** = 0,42
# x*** = 0,87
# x**** = 0,67

def func(x):
    return x**2 + log(x)

a = 0.4
b = 0.9
nodes = [3, 10, 25, 40, 50, 70]
for n in nodes:
    values_x = linspace(a, b, num=n)
    values_y = [func(y) for y in values_x]
    print("VALUES X = ", values_x)
    print("VALUES Y = ", values_y)
    print("SIGMA SUM VALUE = ", SigmaSum(n, values_y, values_x, 0.52))

