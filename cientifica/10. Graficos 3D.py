# Gráficos en python

import matplotlib.pyplot as plt
import numpy as np

# definamos un dominio

x = np.linspace(0,20,num = 200)
y = 4.32*np.sin(x)*np.exp(-0.36*x+0.25418*np.cos(0.4136*x-2.0236))

plt.plot(x,y,'-')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid(ls = 'dashed')

# Podemos colocar anotaciones en el gráfico
plt.annotate('Máximo local',(1.40,2.68),(7.5,2.5), arrowprops=dict())
plt.annotate('Mínimo local',(4.4,-1.1),(10.0,-0.5), arrowprops=dict())

# Diagrama de barras

eje_x = ['Brasil','Vietnam','Colombia','Indonesia']
eje_y = [55,30,14,12]

plt.bar(eje_x, eje_y, color = 'purple')
plt.ylabel('Café x1000 Tn')
plt.xlabel('Paises')
plt.title('Paises productores de café')

import matplotlib.colors as mcolors

importaciones = [3500,4210,3021,4221,5201]
exportaciones = [6201,6541,3874,4632,5741]

CantidadDatos = len(importaciones)
IndiceBarras = np.arange(CantidadDatos)
ancho = 0.35

plt.bar(IndiceBarras, importaciones, width= ancho, label = 'Importaciones', color = 'Orange')
plt.bar(IndiceBarras + ancho, exportaciones, width= ancho, label = 'Exportaciones', color = 'Olive')
plt.legend()
plt.xticks(IndiceBarras+ancho/2,('2000','2001','2002','2003','2004'))
plt.xlabel('Años')
plt.title('Importaciones y exportaciones de Colombia')

# Barras sobrepuestas

grupos = ['Colombia','México','Perú','Venezuela']
importaciones = [150,220,98,150]
exportaciones = [145,250,137,155]

indice = np.arange(len(grupos))

# Se crean las primeras barras
plt.bar(indice, importaciones, label = 'importaciones')
# Se crean lsa segundas barras
plt.bar(indice, exportaciones, label = 'exportaciones',bottom= importaciones)

# Gráficos de torta

etiquetas = ['China','Turquia','Argentina','Irán','USA','Colombia']
valores = [500000,1100000,98000,68000,60000,50000]
vals = [0,0,0.25,0,0,0.7]
plt.pie(x=valores,labels=etiquetas,autopct = '%1.1f%%',explode=vals)
plt.title('Principales productores de mil de abeja')

# Histogramas

np.random.seed(23)

n_points = 100000
n_bins = 20

x = np.random.randn(n_points)
y = 0.4 * x + np.random.randn(100000) + 15

plt.subplot(1, 2,1) # 2 filas, 1 columna
plt.hist(x, bins=n_bins, color = 'purple', rwidth= .85)
plt.subplot(1,2,2)
plt.hist(y, bins=n_bins, color = 'blue', rwidth= .85)

# Grafos en 3D

# Espacio de representación
ax = plt.axes(projection = '3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()


# Scatter plot

x = np.random.randint(20, size = 60)
y = np.random.randint(15, size = 60)
z = np.random.randint(10, size = 60)

fig = plt.figure(figsize= (8,6))
ax = plt.axes(projection ='3d')
ax.plot3D(x,y,z,'o')
ax.plot3D(5,5,5,'r*')

from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

x = np.arange(-2,2,0.05) 
y = np.arange(-2,2,0.05)
x,y = np.meshgrid(x,y)
z = np.sin(x**2)+.5*np.cos(y**2 )
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

surf = ax.plot_surface(x,y,z,cmap = cm.coolwarm,
                linewidth = 0, antialiased = False)
surf
fig.colorbar(surf, shrink = 0.5, aspect = 5)
plt.show()


# Veamos un gráfico de contorno en 2d

def f(x,y):
    return (1-x / 2+ x**5 + y**3)*np.exp(-x**2 - y**2)

n = 256
x = np.linspace(-3, 3,n)
y = np.linspace(-3, 3,n)
x,y = np.meshgrid(x,y)

plt.contourf(x,y,f(x,y),8,alpha = .85, cmap = 'hot')

c = plt.contourf(x,y,f(x,y),8)
plt.clabel(c, fontsize = 10)

plt.imshow(f(x, y))

# 1.12


