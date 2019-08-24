import numpy as np
from math import e

from scipy.optimize import fsolve


def F(x):
    return np.array([x[0] + (x[0] + x[1]) * e ** (x[0] + x[1]) - 3,
                     x[0] + (2 * x[0] + x[1]) * e ** (2 * x[0] + x[1]) - 4])


def J(x):
    a = x[0]
    b = x[1]
    return np.array([[e ** (a + b) + (e ** (a + b)) * (a + b) + 1, e ** (a + b) + (e ** (a + b)) * (a + b)],
                     [2 * e ** (2 * a + b) + (2 * e ** (2 * a + b)) * (2 * a + b) + 1,
                      e ** (2 * a + b) + (e ** (2 * a + b)) * (2 * a + b)]])


def newton(F, J, x, tol):
    xv = F(x)
    con = 0
    while abs(np.linalg.norm(xv, ord=2)) > tol and con < 100:
        aux = np.linalg.solve(J(x), -xv)
        x = x + aux
        xv = F(x)
        con += 1

    # Here, either a solution is found, or too many iterations
    if abs(np.linalg.norm(xv, ord=2)) > tol:
        con = -1
    return x, con


tol = 10e-6
x, n = newton(F, J, [1, 1], tol)
print("Cantidad de iteraciones: ", n)
print("Calculado por el algoritmo: ", x)
r = fsolve(F, [1, 1], fprime=J, full_output=1)
print("Calculado por la libreria Scipy: ", r[0])
