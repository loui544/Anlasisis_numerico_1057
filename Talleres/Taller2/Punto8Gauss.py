import numpy as np


x = [[2,3,7],[-2,5,6],[8,9,4]]
y = [3,5,8]
def gauss(x,y):
    f = len(y)
    c = np.zeros([f,f+1])
    for i in range (f):
        for j in range (f):
            c[i][j] = x[i][j]
        c[i][f] = y[i]
    for k in range(f):
        t = c[k][k]
        for j in range (k,f+1):
            c[k][j] = c[k][j]/t
        for i in range(k+1,f):
            t = c[i][k]
            for j in range (k, f+1):
                c[i][j] = c[i][j]-t*c[k][j]
    h =np.zeros([f,1])
    h[f-1] = c[f-1][f]

    for i in range(f-2, -1, -1):
        s = 0
        for j in range(i+1,f):
            s += c[i][j]*h[j]
        h[i]=c[i][f]-s
    return h

h = gauss(x,y)
print (" -- Resultado --")
print(h)

def error_relativo(v_obtenido,v_real):
    rta = np.linalg.norm(v_obtenido-v_real)/np.linalg.norm(v_real)
    return rta
rta = error_relativo(h,x)
print("Error Relativo")
print(rta)

def numeroDeCondicion(x):
    num_condicion_inf = np.linalg.cond(x,np.inf)
    print("----")
    print(num_condicion_inf)
    return num_condicion_inf

numeroCondicion = numeroDeCondicion(x)