import numerikLib
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace

def runge_func(x):
    return 1/(1+x**2)
  
n = 10
a = -5
b = 5

x = linspace(-5,5,500)
orig_y = runge_func(x)
plt.plot(x,orig_y, color=[0,1,0])
nmin, nmax = 4,15

def get_sweet_color(n:float, r:int, g:int, b:int, scalar:float=1):
    result = []
    for factor in [r,g,b]:
        if factor == 0:
            result.append(0)
        elif factor == -1:
            result.append((1-n)*scalar)
        elif factor == 1:
            result.append(n*scalar)
        else:
            print("RGB 'weights' must be -1,0, or 1; got:", factor)
            exit(1)
    return result

for n in range(nmin, nmax+1):
    colorfactor = (n-nmin)/(nmax-nmin+.001)
    xi = linspace(a,b,n)
    yi = runge_func(xi)
    divdiffs = numerikLib.divided_diff(xi, yi)[0,:]
    newton_y = numerikLib.pNewt(xi, divdiffs, x)
    plt.plot(x,newton_y,color=get_sweet_color(colorfactor, 0, 0, 1))
    plt.plot(xi, yi, 'o', color=get_sweet_color(colorfactor, 0, 0, 1))
    
    xi_tscheb = [x for x in numerikLib.make_cheb_xi(a,b,n)]
    yi_tscheb = [runge_func(x) for x in xi_tscheb]
    
    divdiffs_tscheb = numerikLib.divided_diff(xi_tscheb, yi_tscheb)[0,:]
    newton_y_tscheb = numerikLib.pNewt(xi_tscheb, divdiffs_tscheb, x)
    plt.plot(x,newton_y_tscheb,color=get_sweet_color(colorfactor,1,0,0))
    plt.plot(xi_tscheb, yi_tscheb, 'o', color=get_sweet_color(colorfactor,1,0,0))
plt.plot(xi, yi, 'x', color=[0,1,0])
plt.show()
