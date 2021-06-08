from numpy.polynomial.polynomial import Polynomial
import numerikLib
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

n = 4
a = -5.
b = 5.

def runge_func(x):
    return 1. / (1. + x**2)

def solve_moments(h, f):
    pass
class overengineered:
    def __init__(self, coeffs, xi) -> None:
        self.xi = xi
        self.coeffs = coeffs
    def __call__(self, x):
        return self.coeffs[0]*(x-self.xi)**3 + \
                self.coeffs[1]*(x-self.xi)**2 + \
                self.coeffs[2]*(x-self.xi) + \
                self.coeffs[3]

def s_i(mi, fi, hi, xi, i):
    pass
# def spline(...):
    # bitte ergänzen

xi = [0,1,2,3]
fi = [0,1,0,1]
x = np.linspace(a,b,100)
n=4



plt.plot(xi, fi, 'x', color=[0,1,0])
for interppart in yi:
    plt.plot(x, interppart(x), color=[1,0,1])
plt.show()
