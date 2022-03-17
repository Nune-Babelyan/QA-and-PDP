#!/usr/bin/env python3

import math

def circle(r):
    if r <= 0:
        print ('The radius of the circle cannot be negative number or 0')
    else:
        d = 2 * r
    
        c = d * math.pi
    
        s = r**2 * math.pi
        print ('d = ', d)
        print ('c = ', format (c, '.2f'))
        print ('s = ', format(s, '.2f'))


r = input ('Enther a number: ')

try:
    r = int(r)
except ValueError:
    print('You entered is not integer number')
else:
    circle(r)
