import numpy as np
import math
from numpy.polynomial import Polynomial as PowSer

def get_l_poly_part(k, xi):
    '''
    Get the k-th polynomial with zeros at the other xis
    '''
    interps = len(xi)
    l = np.zeros(interps+1)
    l[0] = 1
    for j in range (interps):
        if j!=k:
            l=l*(-xi[j]/(xi[k]-xi[j]))+np.roll(l,1)/(xi[k]-xi[j])
    return l

def L(k, xi, x):
    '''
    Get the y-value at x of the k-th polynomial thourgh interpolation points k.
    '''
    return PowSer(get_l_poly_part(k, xi))(x)

def pLagr(xi,fi):
    '''
    Get the full Lagrange-polynomial, interpolating at xi and f(xi)
    '''
    interps = len(fi)
    l = np.zeros(interps+1)
    for xIndex in range(interps):
        l += fi[xIndex]*get_l_poly_part(xIndex, xi)
    return PowSer(l)

def divided_diff(x, y):
    '''
    Get the divided differences neede to calculate the newton polynomials from x and y values 
    '''
    n = len(y)
    coef = np.zeros([n, n])
    # the first column is y
    coef[:,0] = y
    
    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])
    return coef

def pNewt(xi, ai, x):
    '''
    Bulid the newton polynomial from the divided differences, interpolating at xi and f(xi), and return its y-values
    '''
    c = len(xi) -1
    p = ai[c]
    for i in range(1, c+1):
        p = ai[c-i] + (x-xi[c-i])*p
    return p

def make_cheb_xi(a:int,b:int,n:int):
    '''
    Get the optimal distribution of n interpolation points on the x-axis from a(left) to b(right)
    '''
    center = .5*(a+b)
    offset = .5*(b-a)
    for i in range (n):
        multiplier = math.cos(((2*i+1)/(2*n+2))*math.pi)
        yield center + offset * multiplier 
