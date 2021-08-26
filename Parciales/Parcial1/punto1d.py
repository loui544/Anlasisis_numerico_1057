##Punto fijo
## f(x)=x^3+2x+k
##Ultimo digito documento de identificacion=9
import math 

def f(x,k): return x**3+2*x+k
def puntoFijo(x,k,tol):
    i=0
    ans=f(x,k)
    tramo=abs(ans-x)
    print(ans)
    while(tramo>=tol):
        x=ans
        ans=x/f(x,k)
        print("Iteracion: ",i," Resultado: ",ans)
        i=i+1
        tramo=abs(ans-x)

x=0
k=9
k1=k+math.sqrt(k+2)
k2=k-(1/3)
tol=10**-10
puntoFijo(x,k1,tol)
puntoFijo(x,k2,tol)



    