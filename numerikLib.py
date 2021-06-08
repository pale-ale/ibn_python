import numpy as np
import math

def L(k,xi,x):
    "k-tes Lagrange Basispolynom zu den Stützstellen xi"
    Lx = 1.
    for j in range(len(xi)):
        if j != k:
            Lx *= (x-xi[j])/(xi[k]-xi[j])
    return Lx

def pLagr(xi,fi,x):
    "Lagrange Interpolationspolynom zu den Stützstellen xi mit Stützwerten fi"
    px = 0.
    for j in range(len(xi)):
        px += fi[j]*L(j,xi,x)
    return px

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
    for i in range(n+1):
        multiplier = math.cos(((2*i+1)/(2*n+2))*math.pi)
        yield center + offset * multiplier 
