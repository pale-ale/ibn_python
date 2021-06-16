import math
import numpy as np

l = 0
r = 1

def f(x):
    return math.sin(math.pi*x)

def F(x):
    return -math.cos(math.pi*x)/math.pi

def trapez_integral(func, l:float, r:float, count:int):
    h = (r-l)/(count)
    ysum = 0
    xvals = np.linspace(l, r, count+1)
    yvals = [func(x) for x in xvals]
    for i in range(0,len(xvals)-1):
        yl = yvals[i]
        yr = yvals[i+1]
        ysum += yl + yr
    return ysum * h * .5

def romberg(func, l:float, r:float, count:int):
    result = []
    h = (r-l)
    result.append([(h/2.0)*(func(l)+func(r))])
    for i in range(1,count+1):
        h = h/2.
        sum = 0
        for k in range(1,2**i ,2):
            sum = sum + func(l+k*h)
        rowi = [0.5*result[i-1][0] + sum*h]
        for j in range(1,i+1):
            rij = rowi[j-1] + (rowi[j-1]-result[i-1][j-1])/(4.**j-1.)
            rowi.append(rij)
        result.append(rowi)
    return result

ideal = F(1) - F(0)
print("Ideal:", ideal)

for n in range(1,20):
    integral = trapez_integral(f, l, r, n)
    print("Steps:", n, "\tValue:", integral, "\tError:", abs(ideal - integral))
print("="*20)
for n in range(1,20):
    integral = romberg(f, l, r, n)[-1][-1]
    print("Steps:", n, "\tValue:", integral, "\tError:", abs(ideal - integral))
