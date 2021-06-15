import math
import numpy as np
import matplotlib.pyplot as plt
import numerikLib

n = 10
l = 0
r = 1

ALPHA = 1
KAPPA = 4

def f(x):
    return math.sin(math.pi*x)

def trapez_integral(func, l:float, r:float, count:int):
    h = (r-l)/(count-1)
    ysum = 0
    xvals = np.linspace(l, r, count)
    yvals = [func(x) for x in xvals]
    for i in range(0,len(xvals)-1):
        yl = yvals[i]
        yr = yvals[i+1]
        ysum += (yl + yr)*.5
    return ysum * h

print(trapez_integral(f, l, r, n))
exit()

for i in range(7,n):
    interppointsx = np.linspace(a,b,i+1)
    interppointsy1 = [func1(x) for x in interppointsx]
    interppointsy2 = [func2(x) for x in interppointsx]
    intervalsize = [(interppointsx[i+1] - interppointsx[i]) for i in range(len(interppointsx)-1)]

    yvals1 = [func1(x) for x in xvals]
    yvals2 = [func2(x) for x in xvals]

    moments1 = numerikLib.solve_moments2(intervalsize, interppointsy1, 0, 0)
    moments2 = numerikLib.solve_moments2(intervalsize, interppointsy2, 1, 1)
    interppolys1 = [numerikLib.s_i(moments1, interppointsy1, intervalsize, k) for k in range(i)]
    interppolys2 = [numerikLib.s_i(moments2, interppointsy2, intervalsize, k) for k in range(i)]

    plt.plot(interppointsx, interppointsy1, 'o', color=[0,0.3*(i-7),0])
    plt.plot(interppointsx, interppointsy2, 'x', color=[0,0.3*(i-7),0])

    for pindex in range(len(interppolys1)):
        poly1 = interppolys1[pindex]
        poly2 = interppolys2[pindex]
        _xvals = np.linspace(interppointsx[pindex], interppointsx[pindex+1], 30)
        xshift = np.linspace(-intervalsize[pindex], 0, 30)
        y1 = poly1(xshift)
        y2 = poly2(xshift)
        plt.plot(_xvals, y1, '-.', color=[1, 1-.3*(i-7),0])
        plt.plot(y1, y2, '-', color=[.3*(i-7), .3*(i-7), .3*(i-7)])
        plt.plot(_xvals, y2, '-.', color=[0, .6, .3*(i-7)])

plt.plot(xvals, yvals1, color=[1,0,0])
plt.plot(xvals, yvals2, color=[0,0,1])
plt.show()
