vfrom scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange
import math

def punto2():
  x = [0, 1, 2]
  y = [10, 15, 5]
  f = interpolate.CubicSpline(x, y, bc_type=((1, 1), (1, 1)))
  xs = np.arange(-0.5, 2.5, 0.1)
  print(str(f))
  plt.plot(x, y,'o',xs, f(xs), '--')
  plt.legend(["Datos","Interpolacion"])
  plt.show()

def func(x):
    return np.tan(x)

def punto6():
    ini = -1.4
    step = 0.8
    xs = np.arange(ini, ini + (step * 10), step)
    f = lagrange(xs, func(xs))
    while abs(func(0) - f(0)) > 10e-2:
        xs = np.arange(ini, ini + (step * 10), step)
        f = lagrange(xs, func(xs))
        step -=0.06
    step +=0.06
    xi = np.arange(ini, ini + (step * 10), 0.1)

    plt.plot(xs, func(xs), 'x', xi, f(xi))
    plt.show()
    return step
def func2(x):
    return math.e**(x)

def punto7():
    ini=1
    x=np.arange(0,1,ini)
    y=math.e**(x)
    f=lagrange(x,y)
    while abs(f(0.5)-func2(0.5)) > 10e-5:
        ini -=0.01
        x = np.arange(0, 1, ini)
        y = math.e ** (x)
        f = lagrange(x, y)
    return ini





print("La solucion del punto 2 es: ")
punto2()
print("El sigma que minimiza el error es : ", punto6())
print("El paso que minimiza el error es : ",punto7())

