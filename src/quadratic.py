'''Quadratic.py- solves ax**2+bx+c=0 and returns the result(s)'''

import cmath as cm

a = float(input('Enter the coefficient on x-squared: '))
b = float(input('Enter the coefficient on x: '))
c = float(input('Enter the constant term: '))
 


discr = b**2 - 4*a*c 

if discr < 0:
    x1 = (-b + cm.sqrt(discr)) / (2*a)
    x2 = (-b - cm.sqrt(discr)) / (2*a)
    print(x1,x2)



