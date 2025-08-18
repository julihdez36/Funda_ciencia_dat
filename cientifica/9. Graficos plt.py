
import numpy as np
import matplotlib.pyplot as plt

# Las gráficas pueden pensarse como un dominio (array) frente a un rango (array)

D = np.array([1,3,4,5,6])
plt.plot(D) # Lo asume como el rango e indexa en una serie ordenada

R = np.array([5,-8,6,1,0])
plt.plot(D,R, 'o-')
plt.plot(D,R, 'o')
plt.plot(D,R, '--')

# Se pueden explorar diferentes opciones

plt.plot(D,R, 'o-', color = 'purple')

x = np.linspace(0, 2*np.pi,100) # de 0 a 2pi
y = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y2, color = 'orange', label = '$\cos x$')
plt.plot(x,y, color = 'red', label = '$\sin x$')
plt.title('Funciones trigonométricas')
plt.xlabel('$x$') # formato latez
plt.ylabel('$y$')
plt.grid(ls = 'dashed')
plt.legend()

# Si quiero los gráficos separados 

plt.figure()
plt.plot(x,y2, color = 'orange', label = '$\cos x$')
plt.title('Funciones trigonométricas')
plt.xlabel('$x$') # formato latez
plt.ylabel('$y$')
plt.grid(ls = 'dashed')
plt.legend()

plt.figure()

plt.plot(x,y, color = 'red', label = '$\sin x$')
plt.title('Funciones trigonométricas')
plt.xlabel('$x$') # formato latez
plt.ylabel('$y$')
plt.grid(ls = 'dashed')
plt.legend()

# O si quiero los gráficos como un subplot
y3 = y + y2
y4 = y**2

plt.subplot(2,2,1) # fila, columna, gráfico
plt.plot(x,y2, color = 'orange', label = '$\cos x$')
plt.title('Función Coseno')
plt.xlabel('$x$') # formato latez
plt.ylabel('$y$')
plt.grid(ls = 'dashed')
plt.legend()

plt.subplot(2,2,2) # fila, columna, gráfico
plt.plot(x,y, color = 'red', label = '$\sin x$')
plt.title('Función Seno')
plt.xlabel('$x$') # formato latez
plt.ylabel('$y$')
plt.grid(ls = 'dashed')
plt.legend()

plt.subplot(2,2,3) # fila, columna, gráfico
plt.plot(x,y3, color = 'purple', label = '$\sin x$')
plt.title('Función $\sin + \cos$')
plt.xlabel('$x$') # formato latez
plt.ylabel('$y$')
plt.grid(ls = 'dashed')
plt.legend()

plt.subplot(2,2,4) # fila, columna, gráfico
plt.plot(x,y4, color = 'purple', label = '$\sin x$')
plt.title('Función $\sin^{2}x$')
plt.xlabel('$x$') # formato latez
plt.ylabel('$y$')
plt.grid(ls = 'dashed')
plt.legend()

