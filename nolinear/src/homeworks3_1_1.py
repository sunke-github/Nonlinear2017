import numpy as n
import scipy as s
import pylab as p

xa=-5
xb=5

A=n.linspace(xa,xb,100)
iteration=100
Y = n.ones(len(A))

for x in range(iteration):
    #Y = Y**2 - A   #get rid of early transients
    Y = A*Y/(1+Y**2)
    #p.plot(A,Y, '-', color = 'b', markersize = 2)

for x in range(iteration): 
    #Y = Y**2 - A
    Y = A*Y/(1+Y**2)
    p.plot(A,Y, '-', color = 'g', markersize = 2)
p.title('homework3-1-1')
p.xlabel('r')
p.ylabel('x')
p.grid(True)
p.show()