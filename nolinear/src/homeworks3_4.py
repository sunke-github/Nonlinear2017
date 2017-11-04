import numpy as n
import scipy as s
import pylab as p

xa=-2
xb=3

C=n.linspace(xa,xb,100)
iteration=1
Y = n.ones(len(C))-1.1

for x in range(iteration):
    #Y = Y**2 - C    #get rid of early transients
    Y = C*Y*(1-Y)
for x in range(iteration): 
    #Y = Y**2 - C 
    Y = C*Y*(1-Y)
    p.plot(C,Y, '.', color = 'k', markersize = 2)

p.show()