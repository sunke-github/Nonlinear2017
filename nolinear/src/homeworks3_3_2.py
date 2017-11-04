
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import numpy as np
import time
#from numpy.distutils.misc_util import colour_text
#from OpenGL._bytes import maxsize

def pend(d0,t,a,b,c,r):
    x,y,z=d0
    dydt=[a*(y-x),b*(x*z-y),c*(r+1-z-r*x*y)]
    return dydt

a = 1/3
b = 1/10
c = 1/20
rspan = np.linspace(5,15,400)
d0 = [0.1,0.1,0.1]
t= np.linspace(0,100,200)

for r in rspan:
    sol = integrate.odeint(pend,d0,t,args=(a,b,c,r))
    first = time.time()
    tarray = np.ones(len(sol[:,0]))
    tarray = tarray * r
    plt.plot(tarray,sol[:,0],'.',color = 'g',markersize = 0.5)
    
plt.show()
