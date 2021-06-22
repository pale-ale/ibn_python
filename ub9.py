from types import FunctionType
import numpy as np
import matplotlib as plt

def newton_verfahren(f:"FunctionType[int]", deriv_f:"FunctionType[int]", x_0:float):
    last = x_0
    while True:
        diff = abs(x_0 - last)
        x_0 = x_0 - f(x_0)/deriv_f(x_0)
        residuum = abs(f(x_0))
        yield residuum, diff

def f(x):
    return np.math.atan(x)

def deriv_f(x):
    return 1/(1 + x**2.0)

X0, X2, X3 = (1,2,1.391745200270735)
TOL = 1.e-8
gen = newton_verfahren(f, deriv_f, X3)
residuum, diff = gen.__next__()
iter = 0
while iter < 100 and residuum > TOL:
    print(f"residuum: {residuum:06.15f}   [@]   diff: {diff:06.15f}")
    iter += 1
    residuum, diff = gen.__next__()

print("=>", residuum)

