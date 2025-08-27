# Métricas estadísticas

import random
import statistics

# Creación del vector


random.uniform(10, 100)

vector = []
for _ in range(10):
    vector.append(random.uniform(10, 100))

vector

# Suma del vector

def suma_interna(x):
    suma = 0
    for i in x:
        suma += i
    #   suma = suma + i
    return suma

sum(vector)
suma_interna(vector)

# Media del vector

def media(x): 
    media = suma_interna(x) / len(x)
    return media

media(vector)

statistics.mean(vector)

# Mediana del vector

def mediana(x):
    x.sort()
    n = len(x)
    if n % 2 != 0:
        return x[n // 2]
    else:
        medio1 = x[n // 2 - 1]
        medio2 = x[n // 2]
        return (medio1 + medio2) / 2

        
mediana(vector)
statistics.median(vector)

# Rango

def rango(x):
    x.sort()
    minimo = x[0]
    maximo = x[-1]
    return maximo - minimo

rango(vector)

# Varianza







