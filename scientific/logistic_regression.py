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

# =====================
# 5. Entrenamiento con descenso de gradiente
# =====================
n_samples, n_features = X_train.shape
theta = np.zeros(n_features)   # inicialización de parámetros

lr = 0.1       # tasa de aprendizaje
epochs = 1000  # número de iteraciones

for i in range(epochs):
    z = X_train @ theta
    h = sigmoid(z)                 # probabilidades predichas
    error = h - y_train             # vector de errores
    grad = (X_train.T @ error) / n_samples  # gradiente promedio
    theta -= lr * grad              # actualización
    
    if i % 100 == 0:
        # función de pérdida (log loss)
        loss = -(y_train*np.log(h+1e-8) + (1-y_train)*np.log(1-h+1e-8)).mean()
        print(f"Iter {i}: loss={loss:.4f}")

# =====================
# 6. Evaluación
# =====================
probs = sigmoid(X_test @ theta)
y_pred = (probs >= 0.5).astype(int)

accuracy = (y_pred == y_test).mean()
print("Accuracy en test:", accuracy)
print("Theta aprendidos:", theta)

