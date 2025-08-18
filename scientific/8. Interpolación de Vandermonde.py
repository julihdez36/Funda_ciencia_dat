'''
Resolvamos el problema de interpolación de Vandermonde:
    
    Dado un conjunto de puntos en R2, queremos encontrar un polinomio que pase por los puntos.
    Se trata entonces de hallar un polinomia de grado 4 (es un grado menor al número de puntos).
    Dado que nos da unas coordenadas, el problema se convierte en resolver un sistema de ecuaciones
    que satisface las coordenadas al evaluar la función.
    
    Ese sistema se conoce como la Matriz de Vandermonde.
    La idea es encontrar el polinomio.
    
    Nota: esta no es la manera mas eficiente, ya que la interpolación de lagrange lo es.
    Pero el ejercicio resulta util.

'''

import numpy as np
import matplotlib.pyplot as plt

# Definamos las coordenadas

x = np.array([2,3,4,5,6])
y = np.array([2,6,5,5,6])
n = len(x)

print('Los puntos \n')

for i in range(n):
    print(f'({x[i]},{y[i]})')
    
# Necesitamos una matriz vacia

V = np.array([], dtype = float)

for i in range(n):
    nv = np.power(x,i)
    V = np.concatenate((V,nv))
    
V = np.reshape(V,(n,n)).T

# Ahora si, resolvamos el sistema

sol = np.linalg.solve(V, y)
sol

solinv = sol[::-1] # Tenemos que invertirlo
p = np.poly1d(solinv)
p #estos son los coeficientes de los polinomios

# Vamor ahora a graficarlo

xp = np.linspace(np.min(x), np.max(x),num = 200)
yp = p(xp)

plt.plot(x,y,'o') # Puntos
plt.title('Polinomio interpolador (Vandermonde)')
plt.plot(xp,yp) # Polinomio calculado
plt.grid(ls = 'dashed')
plt.show()
