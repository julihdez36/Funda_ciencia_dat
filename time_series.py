# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 10:51:59 2025

@author: Julian
"""

'''
Ventana temporal
Frecuencia de recolección: espaciado de los registros


'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ts1 = sns.load_dataset('dowjones')

type(ts1)

plt.plot(ts1.Date, ts1.Price);

'''
Las ts suelen analizarse en tres componentes:
    1. Tendencia-ciclo: la dirección a largo plazo
    2. Estacionalidad: el comportamiento periódico
    3. Residuo: las fluctuaciones irregulares 

'''

time = np.arange(144) # secuencia del 0 al 143

# Componente tendencial

trend = time * 2.65 + 100 # combinación lineal
 
plt.plot(time, trend)
plt.title('Tendencia vs tiempo')
plt.xlabel('Meses')
plt.ylabel('Número de pasajeros [Tendencia]')
plt.grid(linestyle = '--')
plt.show()

# Componente estacional

seasonal = 20 + np.sin(time * 0.5) * 20

plt.plot(time, seasonal)
plt.title('Estacionalidad vs tiempo')
plt.xlabel('Meses')
plt.ylabel('Número de pasajeros [Tendencia]')
plt.grid(linestyle = '--')
plt.show()

# Componente aleatorio

residuals = np.random.normal(loc = 0, scale = 3, size = len(time))

plt.plot(time, residuals)
plt.title('Residuos vs tiempo')
plt.xlabel('Meses')
plt.ylabel('Número de pasajeros [Tendencia]')
plt.grid(linestyle = '--')
plt.show()


'''
Modelos de descomposición y composición de series:
    
    1. Descomposición aditiva
    2. Descomposición multiplicativa
    
'''

# Modelo aditivo

trend_residual = trend + residuals
plt.plot(trend_residual)

trend_seasonal = trend + seasonal 
plt.plot(trend_seasonal)

additive = trend + seasonal + residuals
plt.plot(additive)

multiplicative = trend * seasonal * residuals
plt.plot(multiplicative)

fig, ax = plt.subplots(2,1)
ax[0].plot(additive)
ax[0].set_title('Composición aditiva')
ax[1].plot(multiplicative)
ax[1].set_title('Composición multiplicativa')
plt.tight_layout()





