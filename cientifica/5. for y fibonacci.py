'''
Generemos la serie de Fibonacci

La ida básica es que cada número es la suma de los dos anteriores, comenzando con 0 y 1.

'''

def fibonacci_for(n):
    """Genera los primeros n términos de la serie de Fibonacci usando un bucle for."""
    a, b = 0, 1
    serie_fib = []
    for _ in range(n):
        serie_fib.append(a)
        a, b = b, a + b
    return serie_fib

# Ejemplo de uso
n = 10
print(f"Los primeros {n} términos de Fibonacci usando 'for' son: {fibonacci_for(n)}")


import matplotlib.pyplot as plt

# Generamos los primeros 10 términos de la serie
n = 10
numeros_fib = fibonacci_for(n)

# Creamos una lista de los índices (para el eje X)
indices = list(range(n))

# Creamos el gráfico
plt.figure(figsize=(10, 6)) # Define el tamaño del gráfico
plt.plot(indices, numeros_fib, marker='o', linestyle='-', color='b')

# Añadimos títulos y etiquetas
plt.title('Crecimiento de la Serie de Fibonacci', fontsize=16)
plt.xlabel('Término de la Serie', fontsize=12)
plt.ylabel('Valor del Término', fontsize=12)
plt.grid(True)
plt.xticks(indices, labels=[str(i) for i in indices]) # Asegura que los ticks sean enteros

# Mostramos el gráfico
plt.show()