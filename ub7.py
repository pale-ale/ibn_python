import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math
import numerikLib

n = 10
a = 0.
b = 2.*np.pi

ALPHA = 1
KAPPA = 2

def func1(t):
    return ALPHA*math.cos(KAPPA*t)*math.cos(t)

def func2(t):
    return ALPHA*math.cos(KAPPA*t)*math.sin(t)

xvals = np.linspace(a,b,100)

for i in range(7,n):
    interppointsx = np.linspace(a,b,i+1)
    interppointsy1 = [func1(x) for x in interppointsx]
    interppointsy2 = [func2(x) for x in interppointsx]
    intervalsize = [(interppointsx[i+1] - interppointsx[i]) for i in range(len(interppointsx)-1)]

    yvals1 = [func1(x) for x in xvals]
    yvals2 = [func2(x) for x in xvals]

    moments1 = numerikLib.solve_moments2(intervalsize, interppointsy1)
    moments2 = numerikLib.solve_moments2(intervalsize, interppointsy2)
    interppolys1 = [numerikLib.s_i(moments1, interppointsy1, intervalsize, k) for k in range(i)]
    interppolys2 = [numerikLib.s_i(moments2, interppointsy2, intervalsize, k) for k in range(i)]

    plt.plot(interppointsx, interppointsy1, 'o', color=[0,0.3*(i-7),0])
    plt.plot(interppointsx, interppointsy2, 'x', color=[0,0.3*(i-7),0])

    for pindex in range(len(interppolys1)):
        poly1 = interppolys1[pindex]
        poly2 = interppolys2[pindex]
        _xvals = np.linspace(interppointsx[pindex], interppointsx[pindex+1], 30)
        xshift = np.linspace(-intervalsize[pindex], 0, 30)
        plt.plot(_xvals, poly1(xshift), '-.', color=[1, 1-.3*(i-7),0])
        plt.plot(_xvals, poly2(xshift), '-.', color=[0, .6, .3*(i-7)])

plt.plot(xvals, yvals1, color=[1,0,0])
plt.plot(xvals, yvals2, color=[0,0,1])
plt.show()
