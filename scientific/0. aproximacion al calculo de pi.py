# Aproximaciones a Pi: montecarlo y serie de Leibniz

''''
Progama para calcular pi con el método de Montecarlo:
    
Inscribimos una circunferencia en un cuadrado de lados l. Siendo así,
sabemos que el radio de la circunferencia se define.

Podemos definir la siguiente equivalencia:
    (points_in_circle / total_points) = (Area_circle / Area_square)

Recordemos que:
    Area_circle = pi * r^2
    Area_square = (2*r)^2 = 4*r^2 

Entonces, retomando la equivalencia:
    (points_in_circle / total_points) = (pi * r^2) / (4 * r^2)
    (points_in_circle / total_points) = pi / 4
    
    
Despejando Pi:
    
    pi = 4 * (points_in_circle / total_points)


'''

import math
import random

# Definimos una variable del número de puntos

# Creamos nuestra fución

def pi_montecarlo(n):
    pdentro = 0
    
    for i in range(n):
        # Generamos coordenadas aleatorias entre 0 y 1
        x= random.uniform(0, 1) # Distribución uniforme [0,1]
        y= random.uniform(0, 1)
        
        # Calculemos ahora la distancia euclidiana al origen con pitagoras
        distancia = math.sqrt(x**2 + y**2)
        
        if distancia <= 1: # si el radio es menor que 1
            pdentro += 1
            
    # Calculamos ahora la proporción
    proporcion = pdentro / n
    
    pi_estimado = 4*proporcion
    
    return pi_estimado


# Evaluemos ahora con diferentes valores de n


for i in [100,1000,10000, 100000]:
    n = i
    pi_est = pi_montecarlo(n)
    print(f'El valor estimado de pi con {i} puntos es: {pi_est}, con un error de: {pi_est - math.pi}')


# ------------------------------------------------------------------------
# probemos una segunda forma a través de la serie de Leibniz

'''
La seri de Leibniz se puede establecer como una serie infinita de la forma:
    
    4 * \sum_{n=0}^{infty} \frac{-1}^{n}{2n+1}= \pi
    
''''


def leibniz_serie(n):
    serie = []
    for i in range(n):
        num = (-1)**i
        den = 2*i +1
        cociente = num/den
        serie.append(cociente)
    return 4 * sum(serie)
        
n = 10

leibniz_serie(n)        
        
for i in [100,1000,10000, 100000]:
    n = i
    pi_est = leibniz_serie(n)
    print(f'El valor estimado de pi con {i} puntos es: {pi_est}, con un error de: {pi_est - math.pi}')

        
        
        
        
        
        
        
        
        

  

