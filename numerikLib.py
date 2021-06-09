import numpy as np
import math

def runge_func(x):
    return 1. / (1. + x**2)

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

def solve_moments(h, f):
    '''
    Solve moments with natural borders
    '''
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

def solve_moments2(h, f):
    '''
    Solve moments with exercise07's borders
    '''
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
    mborder = 6/(h[-1]+h[0])*((f[0]-f[-1])/h[0] - (f[-1]-f[-2])/h[-1])
    linequation[0][0] = 2
    linequation[0][1] = mborder
    linequation[-1][-1] = 2
    linequation[-1][-2] = mborder
    return np.linalg.solve(linequation, rightside)

def s_i(mi, fi, hi, i):
    a0, a2 = fi[i+1], mi[i+1]/2
    a1 = (fi[i+1]-fi[i])/hi[i] + ( hi[i] * (2.0*mi[i+1] + mi[i]) )/6.0
    a3 = (mi[i+1] - mi[i]) / (6*hi[i])
    poly = np.polynomial.Polynomial((a0, a1, a2, a3))
    return poly
