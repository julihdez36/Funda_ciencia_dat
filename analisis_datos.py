# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 09:20:57 2025

@author: Julian
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('penguins')

df.shape
df.columns

df.info()

df.species.unique()
df.island.unique()
df.sex.unique()

# Revisemos los NA

df.isna().sum()

# Visualizaciones sobre variables cualitativas

### Gráficos de barras y los gráficos de sectores

# (df.species == 'Adelie').sum()

df.species.value_counts().index

label_x = df.species.value_counts().index
height = df.species.value_counts().values

# Gráficos de barras
plt.bar(label_x, height)
plt.ylabel('Frecuencia')
plt.xlabel('Especies')
plt.title('Frecuencia de aparición por especie')
plt.grid(linestyle = '--')
plt.show()

# Gráfico de sectores [pie chart]

df.species.value_counts(normalize = True) * 100

plt.pie(height, labels = label_x, autopct= '%1.2f%%',
        explode = (0,0,0.2), colors = ('#dfb16e',
                                       'lightcoral',
                                       'lightskyblue'),
        shadow = True, startangle= 90)
plt.show()

# Combinación de variables cualitativas con cuantitativas

df.columns

tabla = df.groupby('species')['bill_length_mm'].mean()
tabla.index
tabla.values

plt.bar(tabla.index, tabla.values, color = 'purple')
plt.ylabel('Promedio de la longitud del pico (mm)')
plt.xlabel('Especies')
plt.title('Longitud de pico por especie')
plt.grid(linestyle = '--')
plt.show()


# Boxplot

df = df[df.bill_length_mm.isna() == False]
df.isna().sum()

plt.boxplot(df.bill_length_mm)

sns.boxplot(data = df, x = 'species', y = 'bill_length_mm',
            palette = 'rainbow')
plt.title('Especies por longitud de pico')







