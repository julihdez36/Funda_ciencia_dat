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

# Modelos multiplicativo

multiplicative = trend * seasonal * residuals
plt.plot(multiplicative)

fig, ax = plt.subplots(2,1)
ax[0].plot(additive)
ax[0].set_title('Composición aditiva')
ax[1].plot(multiplicative)
ax[1].set_title('Composición multiplicativa')
plt.tight_layout()


#### Descomposición de las series de tiempo

slope, intercept = np.polyfit(np.arange(len(additive)), additive, 1) # estimate line coefficient
trend = np.arange(len(additive)) * slope + intercept # linear trend
detrended = additive - trend # remove the trend

plt.figure(figsize=(8, 3))
plt.plot(additive, label='Original')
plt.plot(trend, label='Trend')
plt.plot(detrended, label='Detrended')
plt.grid()
plt.legend();


from statsmodels.tsa.seasonal import seasonal_decompose


additive_decomposition = seasonal_decompose(x=additive, model='additive', period=12)

def seas_decomp_plots(original, decomposition):
    _, axes = plt.subplots(4, 1, sharex=True, sharey=False, figsize=(7, 5))
    axes[0].plot(original, label='Original')
    axes[0].legend(loc='upper left')
    axes[1].plot(decomposition.trend, label='Trend')
    axes[1].legend(loc='upper left')
    axes[2].plot(decomposition.seasonal, label='Seasonality')
    axes[2].legend(loc='upper left')
    axes[3].plot(decomposition.resid, label='Residuals')
    axes[3].legend(loc='upper left')
    plt.show()  

seas_decomp_plots(additive, additive_decomposition)


from statsmodels.tsa.seasonal import STL


stl_decomposition = STL(endog=additive, period=12, robust=True).fit()
seas_decomp_plots(additive, stl_decomposition)


### Estacionariedad

# Imports

from io import BytesIO
import requests
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import quad
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
np.random.seed(0) # Reproducibility

def run_sequence_plot(x, y, title, xlabel="Time", ylabel="Values", ax=None):
    if ax is None:
        _, ax = plt.subplots(1,1, figsize=(10, 3.5))
    ax.plot(x, y, 'k-')
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(alpha=0.3)
    return ax


T = 200
time = np.arange(T)
stationary = np.random.normal(loc=0, scale=1.0, size=(T))

ax = run_sequence_plot(time, stationary, title="Stationary TS")
ax.plot(time, np.ones_like(time)*np.mean(stationary), linewidth=2, color='tab:red', label='Mean');
ax.fill_between(time, np.ones_like(time)*(stationary.mean()-1.96*stationary.std()), 
                np.ones_like(time)*(stationary.mean()+1.96*stationary.std()), 
                color='tab:red', alpha=0.2, label='std')
plt.legend();



ar1 = np.array([1, -0.8]) 
ma1 = np.array([1])
AR_object1 = ArmaProcess(ar1, ma1)
constant_autocorr_ts = AR_object1.generate_sample(nsample=200)

run_sequence_plot(time, constant_autocorr_ts, 
                  title="Time series with constant autocorrelation ($X$)");



ar2 = np.array([1, -0.9]) 
AR_object2 = ArmaProcess(ar2, ma1)
ar3 = np.array([1, 0.3]) 
AR_object3 = ArmaProcess(ar3, ma1)

time_dependent_autocorr_ts_1 = AR_object2.generate_sample(nsample=100)
time_dependent_autocorr_ts_2 = AR_object3.generate_sample(nsample=100)
time_dependent_autocorr_ts = np.concatenate([time_dependent_autocorr_ts_1, 
                                             time_dependent_autocorr_ts_2])

run_sequence_plot(time, time_dependent_autocorr_ts, 
                  title="Time series with time-dependent autocorrelation ($Y$)");














