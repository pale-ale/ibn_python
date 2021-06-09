from numpy.core.function_base import linspace
import numerikLib
import numpy as np
import matplotlib.pyplot as plt

n = 5
a = -5.
b = 5.

interppointsx = np.linspace(a,b,n+1)
interppointsy = numerikLib.runge_func(interppointsx)

interppointsxc = [x for x in numerikLib.make_cheb_xi(a,b,n)]
interppointsyc = [numerikLib.runge_func(x) for x in interppointsxc]

intervalsize = [(interppointsx[i+1] - interppointsx[i]) for i in range(len(interppointsx)-1)]
intervalsizec = [(interppointsxc[i+1] - interppointsxc[i]) for i in range(len(interppointsxc)-1)]

moments = numerikLib.solve_moments(intervalsize, interppointsy)
momentsc = numerikLib.solve_moments(intervalsizec, interppointsyc)

interppolys = [numerikLib.s_i(moments, interppointsy, intervalsize, i) for i in range(n)]
interppolysc = [numerikLib.s_i(momentsc, interppointsyc, intervalsizec, i) for i in range(n)]

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
 