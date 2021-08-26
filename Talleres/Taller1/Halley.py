import math
global h
h = 0.00000001
eps = 10**-8

# f(x) to solve
def fA(x):return math.cos(x)**2-x**2

def fp(x):
    global h
    return (fA(x + h) - fA(x)) / h

def fpp(x):
    global h
    return (fp(x + h) - fp(x)) / h

# main
x = 2.0 # initial value

while True:
    fx = fA(x)
    fpx = fp(x)
    xnew = x - (2.0 * fx * fpx) / (2.0 * fpx * fpx - fx * fpp(x))
    print (xnew)
    if abs(xnew - x) <= eps: break
    x = xnew