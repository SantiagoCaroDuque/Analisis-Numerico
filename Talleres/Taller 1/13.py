# n --> potencia de la raiz
# a --> Numero de la raiz
# E --> Tolerancia
# x --> Valor inicial


def nth_root(a,n, x, E):
    con=0
    r = (1 / n) * ((n - 1) * x + (a / potencia(x, n - 1)))
    while abs(r-x) > E:
        con=con+1
        x=r
        r = (1 / n) * ((n - 1) * x + (a / potencia(x, n - 1)))
    return r,con



def potencia(num, pot):
    r = num
    for i in range(pot - 1):
        r = r * num
    return r


print(potencia(2, 3))
print(nth_root(25,2,0.0001,0.1))
