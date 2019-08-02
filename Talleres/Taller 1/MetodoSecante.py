import math
import matplotlib.pyplot as plot


gx=[]
gy=[]
def funcion(x):
    return math.e ** (x) - math.pi * x
def derivada(x):
    return 3*(x-(9784/5000))**2

def newton(E,x,a,b):
    err=math.inf
    con=0
    while(err>E):
        if con>0:
            gx.append(err)
        con=con+1
        nx=x-(funcion(x)/(funcion(b)-funcion(a))/b-a)
        err=abs(nx-x)
        if con>1:
            gy.append(err)
        x=nx
    return format(nx, ".10g"),con

print(newton(0.0000001, 0,0,1))
plot.scatter(gx,gy)
plot.show()
