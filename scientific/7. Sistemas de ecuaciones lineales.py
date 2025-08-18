
# Sistemas de ecuaciones lineales

import numpy as np

# Empecemos con R1

num = np.float32(5.123324293456) # mayor capacidad que la de un real

print('%.10f' %(num)) # son muas precisos, pero ocupan mas memoria

# En R2 creemos un vector

vec = np.array([1,2,3,4,5]) # ya no es una lista, es un vector
# No se diferencia entre un vector fila y uno columna

# También podemos crear un vector desde una lista
lista = list(range(1,5))
vec2 = np.array(lista)

# En Rn con n>2

matriz = np.array([[1,2,3],
                  [5,6,7],
                  [8,9,10]])

print(matriz)

vec3 = np.linspace(0,10,30)
vec3 # este es un vector, no una matriz

len(vec3)
np.shape(vec3), vec3.shape

# También puedo sacar un vector con espaciado logaritmico

vec4 = np.logspace(1,10,50)
vec4

# Algebra de matrices

a = np.array([1,2,3])
b = np.array([5,6,-2])

# Operaciones vectorizadas
a+b
a*b
a/b
a**2 

# Producto escalar o producto punto
a@b
# Calculo de la norma
np.linalg.norm(a)

# Operaciones con matrices

m1 = np.array([[2,5,7],
               [-9,2,1],
               [3,-4,-1]])

m2 = np.array([[-8,7,1],
               [0,5,-9],
               [7,5,-3]])

# Operaciones punto a punto
m1+m2   
m1*m2 

# Operaciones matriciales
m1@m2 

I = np.identity(3)
I

m2 @ np.linalg.inv(m2) # Identidad como resultado

# Determinante

np.linalg.det(m1)

# Matriz inversa

np.linalg.inv(m2)



## Cómo resolver un sistema AX=B
# Requerimos una matriz invertible y un vector

b = np.array([4,6,-8])
m1

np.linalg.solve(m1, b) # solución del sistema AX=B

# Resolvamos un sistema mas grande

# Podríamos importarla así
# np.loadtxt('file.txt', dtype=float) # para importar ena matriz

m = np.random.uniform(0,10,(40,40))

m.shape
np.shape(m)

v = np.random.uniform(0,10,(40,))
v.shape

# Solución del sistema
x = np.linalg.solve(m, v)
x

