import math

def f(x):
    return x*math.cos(x)


def derivada(h):
    arriba= f(x0+h)-f(x0)
    return round(arriba/h,8)

h=[0.1,0.01,0.001,0.0001]
x0=1.8

for i in h:
    print(derivada(i))
