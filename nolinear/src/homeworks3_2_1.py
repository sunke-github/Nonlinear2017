import numpy as n
import scipy as s
import pylab as p
import math

b = 0.25
alist = [2.8]
N = 1000
xarray = [0]
yarray = [0]


for a in alist:
    xarray.insert(1, -0.1)
    yarray.insert(1, -0.0001)
    for i in range(1,N):
        xarray.insert(i+1,yarray[i])
        yarray.insert(i+1,a*yarray[i]-b*xarray[i]-pow(yarray[i],3))

p.plot(xarray,yarray,'.',color = 'g', markersize = 2)
p.title('')
p.xlabel('x')
p.ylabel('y')
p.grid(True)
p.show()