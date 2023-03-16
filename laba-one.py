from function import func
from numpy import linspace
from errors import *
import csv
# function x^2 + ln(x);
# [a; b] = [0,4; 0,9]
# x* = 0,52
# x** = 0,42
# x*** = 0,87
# x**** = 0,67

a = 0.4
b = 0.9
nodes = [3, 11, 25, 41, 51, 71]
x_stars =[0.52, 0.42, 0.87, 0.67]
header = ["n", "Aerror", "Rerror", "Terror"]

with open('laba.csv', 'w') as file:
    writer = csv.writer(file, delimiter=";", lineterminator='\n')
    for x_star in x_stars:
        writer.writerow(header)
        for n in nodes:
            values_x = linspace(a, b, num=n)
            values_y = [func(y) for y in values_x]
            absoluteError = calculateAbsoluteError(n, values_x, values_y, x_star)
            relativeError = calculateRelativeError(absoluteError, x_star)
            theoryError = calculateTheoryError(n, x_star, a, b)
            data = [n, absoluteError, relativeError, theoryError]
            writer.writerow(data)

