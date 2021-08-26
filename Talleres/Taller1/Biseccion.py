import decimal
import math
from decimal import *
getcontext().prec=30

def biseccion (f,a,b,e):
    while b-a>=e:
        c=(a+b)/2
        if f(c)==0:
            return c
        else:
            if f(a)*f(c)>0:
                a=c
            else:
                b=c
    return c

tols=[10**-8,10**-16,10**-32,10**-56]
def f(x): return math.cos(x)**2-x**2
for tol in tols:
    eje1=biseccion(f,0,1,tol)
    print("{0}".format(Decimal(eje1)))
    print("{0}".format(Decimal(f(eje1))))

print("\n")
