from numpy.core.function_base import linspace
import numerikLib
import numpy as np
import matplotlib.pyplot as plt

n = 50
a = -5.
b = 5.

def runge_func(x):
    return 1. / (1. + x**2)

def solve_moments(h, f):
    linequation = np.zeros((len(h)+1,len(h)+1))
    rightside = np.zeros(len(h)+1)
    offset = 1
    for i in range(1,len(h)):
        li = 0
        hi = h[i-1]
        hip = h[i]
        linequation[i][offset] = 2
        li = hip/(hi+hip)
        di = 6/(hi+hip) * ( (f[i+1]-f[i])/hip - (f[i]-f[i-1])/hi )
        linequation[i][offset+1] = li
        linequation[i][offset-1] = 1-li
        rightside[i] = di
        offset += 1
    linequation[0][0] = 2
    linequation[0][1] = 0
    linequation[-1][-1] = 2
    linequation[-1][-2] = 0
    return np.linalg.solve(linequation, rightside)

def s_i(mi, fi, hi, xi, i):
    a0, a2 = fi[i+1], mi[i+1]/2
    a1 = (fi[i+1]-fi[i])/hi[i] + ( hi[i] * (2.0*mi[i+1] + mi[i]) )/6.0
    a3 = (mi[i+1] - mi[i]) / (6*hi[i])
    poly = np.polynomial.Polynomial((a0, a1, a2, a3))
    return poly

interppointsx = np.linspace(a,b,n+1)
interppointsy = runge_func(interppointsx)

interppointsxc = [x for x in numerikLib.make_cheb_xi(a,b,n)]
interppointsyc = [runge_func(x) for x in interppointsxc]

intervalsize = [(interppointsx[i+1] - interppointsx[i]) for i in range(len(interppointsx)-1)]
intervalsizec = [(interppointsxc[i+1] - interppointsxc[i]) for i in range(len(interppointsxc)-1)]

moments = solve_moments(intervalsize, interppointsy)
momentsc = solve_moments(intervalsizec, interppointsyc)

interppolys = [s_i(moments, interppointsy, intervalsize, interppointsx, i) for i in range(n)]
interppolysc = [s_i(momentsc, interppointsyc, intervalsizec, interppointsxc, i) for i in range(n)]

plt.plot(interppointsx, interppointsy, 'x', color=[0,1,0])
plt.plot(interppointsxc, interppointsyc, 'o', color=[0,1,0])

for i in range(n):
    poly = interppolys[i]
    xvals = linspace(interppointsx[i], interppointsx[i+1], 30)
    xshift = linspace(-intervalsize[i], 0, 30)
    plt.plot(xvals, poly(xshift), color=[1,0,1])
for i in range(n):
    poly = interppolysc[i]
    xvals = linspace(interppointsxc[i], interppointsxc[i+1], 30)
    xshift = linspace(-intervalsizec[i], 0, 30)
    plt.plot(xvals, poly(xshift), color=[.8,0,0])
plt.show()
 