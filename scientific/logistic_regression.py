# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 20:00:26 2025

@author: Julian
"""
# https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud?resource=download
# Importemos nuestros datos

import numpy as np
import matplotlib.pyplot as plt
import os


os.getcwd()

df = np.loadtxt('scientific\\creditcard.csv', dtype=float, skiprows= 1, delimiter=',') 

type(df)
df.shape 

y = df[:,-1]
y = np.array([int(i) for i in y])

X = df[:,:30]
y.shape, X.shape

n = y.shape[0]

y.ndim
X.ndim

y.size, X.size

etiquetas, conteo = np.unique(y, return_counts= True)

plt.bar(etiquetas, height = conteo, edgecolor="white", linewidth=0.7, color = ['darkblue','orange'])

# =====================
# train, test sample (80/20)
# =====================

idx = list(range(n))
np.random.shuffle(idx)

train_idx = idx[:int(0.8 * n)] # hasta
test_idx = idx[int(0.8 * n):] # Desde

X_train, y_train = X[train_idx], y[train_idx]
X_test, y_test = X[test_idx], y[test_idx]

# =====================
# 3. Preparar datos
# =====================
# Escalamos features para mejor convergencia
mean = X_train.mean(axis=0)
std = X_train.std(axis=0) + 1e-8
X_train = (X_train - mean) / std
X_test = (X_test - mean) / std

# Añadimos intercepto (columna de unos)
X_train = np.c_[np.ones(X_train.shape[0]), X_train]
X_test = np.c_[np.ones(X_test.shape[0]), X_test]

# =====================
# 4. Definir funciones matemáticas básicas
# =====================
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def log_loss(y, h):
    return -(y*np.log(h+1e-8) + (1-y)*np.log(1-h+1e-8)).mean()

# =====================
# 5. Entrenamiento con descenso de gradiente
# =====================

n_samples, n_features = X_train.shape
theta = np.zeros(n_features)

lr = 0.1
epochs = 500

loss_history = []

for i in range(epochs):
    z = X_train @ theta
    h = sigmoid(z)
    error = h - y_train
    grad = (X_train.T @ error) / n_samples
    theta -= lr * grad
    
    # guardar pérdida
    loss = log_loss(y_train, h)
    loss_history.append(loss)

# =====================
# 6. Evaluación
# =====================
probs = sigmoid(X_test @ theta)
y_pred = (probs >= 0.5).astype(int)

accuracy = (y_pred == y_test).mean()
print("Accuracy en test:", accuracy)
print("Theta aprendidos:", theta)

# =====================
# 7. Gráfica de la pérdida
# =====================
plt.plot(loss_history)
plt.xlabel("Época")
plt.ylabel("Log-Loss")
plt.title("Evolución del entrenamiento")
plt.show()


###### Grafico de la función logistica

import numpy as np
import matplotlib.pyplot as plt

# 1. Definir la función logística (sigmoide)
def funcion_logistica(x, L, k, x0):
    """
    Calcula el valor de la función logística.
    
    Parámetros:
    x: array de valores de entrada
    L: valor máximo de la curva (asíntota superior)
    k: tasa de crecimiento (pendiente de la curva en el punto de inflexión)
    x0: valor de x del punto de inflexión (donde la pendiente es máxima)
    """
    return L / (1 + np.exp(-k * (x - x0)))

# 2. Generar datos con NumPy
# Crear un rango de valores para el eje x
x = np.linspace(-10, 10, 400)

# Parámetros de la función logística
L = 1.0  # Asintota superior
k = 1.0  # Tasa de crecimiento
x0 = 0.0 # Punto de inflexión

# Calcular los valores de y utilizando la función
y = funcion_logistica(x, L, k, x0)

# 3. Graficar la función con Matplotlib
plt.figure(figsize=(8, 6)) # Opcional: ajustar el tamaño de la figura
plt.plot(x, y, label=f'L={L}, k={k}, x0={x0}')
plt.title('Función Logística')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True) # Muestra una cuadrícula
plt.legend() # Muestra la leyenda con los parámetros
plt.axhline(y=L, color='r', linestyle='--', label=f'Asintota superior (y={L})') # Muestra la asíntota superior
plt.axhline(y=0, color='r', linestyle='--', label=f'Asintota inferior (y=0)') # Muestra la asíntota inferior
plt.axvline(x=x0, color='g', linestyle='--', label=f'Punto de inflexión (x={x0})') # Muestra el punto de inflexión
plt.show() # Muestra el gráfico
