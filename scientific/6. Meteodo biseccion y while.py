# Definamos una función que utilice el método de bisección
# para calcular las raices de funciones continuas


# primero observemos las ventajas de numpy sobre math
import numpy as np
from math import sin

a = [2,3]

sin(a) # sin no recibe objetos iterables
np.sin(a) # numpy si puede hacer esto. Funciones vectorizada

def f(x):
    y = np.exp(-0.5*np.sinh(x))+ x - 3.2 # una función elegida
    return y

# Definimos intervalo de límite superior e inferiro arbitrario

a = 2.0 
b = 4.0

# Definimos una toleración de error

counter = 0
tolerance = 0.001
x_new = 0.0
error = 0.0

print('%d \t %f \t %f \t %f \t %.8f' %(counter,a,b,x_new,error)) #%d formatea la salida

while abs(a-b) >= tolerance:
    x_new = (a + b)/2.0
    if f(x_new)*f(a) > 0.0:
        a = x_new 
    else:
        b = x_new
    counter += 1
    error = abs(a-b)
    print('%d \t %f \t %f \t %f \t %.8f' %(counter,a,b,x_new,error))
     
print(f'La raiz estimada de de la función es {x_new}, el valor real es 3.91977779078')
    

