def raizCuadrada(n,E,x):
    y=0.5*(x+(n/x))
    while abs(x-y)>E:
        x=y
        y = 0.5 * (x + (n / x))
    return y

print(raizCuadrada(30,0.00000001,2))
