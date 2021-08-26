import math
def f(x): return 2+math.sin(x)-x
def puntoFijo(x,tol):
    i=0
    ans=f(x)
    tramo=abs(ans-x)
    print(ans)
    while(tramo>=tol):
        x=ans
        ans=x/f(x)
        print("Iteracion: ",i," Resultado: ",ans)
        i=i+1
        tramo=abs(ans-x)

x=0
tol=10**-5
puntoFijo(x,tol)