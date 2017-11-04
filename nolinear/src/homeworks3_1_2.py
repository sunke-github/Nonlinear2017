import numpy as n
import scipy as s
import pylab as p
import math
N = 100
x1 = 0.5

alist = n.linspace(-4,4,100)
lmaarray = []
def getXn(i,a):
    n = 1
    xn = x1
    while n <= i:
        xn = a*xn/(1+xn**2)
        n=n+1
    return xn 

for a in alist:
    lma = 0
    for i in range(1,N):
        xn = getXn(i,a)
        e1 = a*(1-xn**2)
        e2 = (1+xn**2)**2
        e3 = e1/e2
        e4 = abs(e3)
        e5 = math.log(e4)
        e6 = 1/N * e5
        lma = lma + e6
    lmaarray.append(lma)
    
p.plot(alist,lmaarray, '-', color = 'g', markersize = 2)
p.title('homework3-1-1')
p.xlabel('a')
p.ylabel('lam')
p.grid(True)
p.show()