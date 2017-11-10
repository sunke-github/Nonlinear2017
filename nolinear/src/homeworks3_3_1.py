
from mpl_toolkits.mplot3d import Axes3D
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import numpy as np

def pend(d0,t,a,b,c,r):
    x,y,z=d0
    dydt=[a*(y-x),b*(x*z-y),c*(r+1-z-r*x*y)]
    return dydt

a = 1/3
b = 1/10
c = 1/20
r = 20
d0 = [0.1,0.1,0.1]

t= np.linspace(0,1000,100000)
sol = integrate.odeint(pend,d0,t,args=(a,b,c,r))

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(sol[:,0], sol[:,1], sol[:,2],label='parametric curve')
ax.legend()
plt.show()
