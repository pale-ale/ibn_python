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
    # B)
    linequation = np.zeros((len(h),len(h)))
    rightside = np.zeros(len(h))
    offset = 1
    for i in range(1,len(h)-1):
        li = 0
        di = 0
        hi = h[i]
        linequation[i][offset] = 2
        li = h[i+1]/(hi+h[i+1])
        di = 6/(hi+h[i+1]) * ( (f[i+1]-f[i])/h[i+1] - (f[i]-f[i-1])/hi )
        linequation[i][offset+1] = li
        linequation[i][offset-1] = 1-li
        rightside[i] = di
        offset += 1
    linequation[0][0] = 2
    linequation[0][1] = 0
    linequation[-1][-1] = 2
    linequation[-1][-2] = 0
    return np.linalg.solve(linequation, rightside)

class overengineered:
    def __init__(self, coeffs, xi) -> None:
        self.xi = xi
        self.coeffs = coeffs
    def __call__(self, x):
        return self.coeffs[0]*((x-self.xi)**3) + \
                self.coeffs[1]*((x-self.xi)**2) + \
                self.coeffs[2]*(x-self.xi) + \
                self.coeffs[3]

def s_i(mi, fi, hi, xi, i):
    # C)
    # Keine Ahnung, wie man hier weitermacht. 
    # Numpy.polynomial kann nur x^3, x^2 ..., wie soll da a(x-x^3) gehen?
    # stimmen die as? wir wissen nicht, wie man das hier gut nachprüfen kann.
    # Die Spline-funktion können wir genauso wenig testen, ich hoffe, das zählt als ernsthaft bearbeitet.
    fi = np.roll(fi, 1)
    a0, a2 = fi[i], mi[i]/2
    a1 = (fi[i]-fi[i-1])/hi[i] + ( hi[i] * (2.0*mi[i] + mi[i-1]) )/6.0
    print("Partials:\ti\tfi[i]\tfi[i-1]\thi[i]\tmi[i]\tmi[i-1]")
    print(f"Partials:\t{i}\t{fi[i]}\t{fi[i-1]}\t{hi[i]}\t{mi[i]}\t{mi[i-1]}")
    a3 = (mi[i] - mi[i-1]) / (6*hi[i])
    print("as:", a0, a1, a2, a3)
    #poly = np.polynomial.Polynomial((a3, a2, a1, a0))
    poly = overengineered([a3, a2, a1, a0], xi[i])
    return poly

# def spline(...):
    # Wir wussten nicht, wie wir das bearbeiten sollen. s.o. (def s_i())
    # bitte ergänzen

xi = np.linspace(a,b,n+1)
x = np.linspace(a,b,100)
xi = [0,1,2,3]
fi = [0,1,0,1]
# Wir haben versucht, die Werte / Herangehensweise von Blatt 6.2 zu nutzen, um zumindest ein paar 
# Werte von Hand ausrechnen zu können. Leider hat das alles trotzdem nicht wirklich hingehauen,
# und wir haben da jetzt an die 5 stunden p.P. reininvestiert ohne wirkliche Lösung.,
# (deswegen sieht hier alles aus wie eine Baustelle)

n=len(xi)-1
#plt.plot(x, f, color=[0,1,0])
# A)
hi = [(xi[i+1] - xi[i]) for i in range(len(xi)-1)]

moments = (solve_moments(hi, fi))
y = np.polynomial.Polynomial(moments)(x)

yi = [s_i(moments, fi, hi, xi, i) for i in range(n)]
#plt.plot(x, y, color=[0,0,1])
plt.plot(xi, fi, 'x', color=[0,1,0])
for interppart in yi:
    plt.plot(x, interppart(x), color=[1,0,1])
plt.show()
