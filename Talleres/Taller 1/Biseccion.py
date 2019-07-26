def funcion(x):
    return x*x+5*x+6

def biseccion(E,s,f):
    if(funcion(s)*funcion(f)<=0):
        print("El intervalo no sirve")