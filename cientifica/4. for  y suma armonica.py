
'''
La suma armónica de orden n, denotada como H_n, es la suma de los recíprocos de los primeros n números enteros positivos.
 
'''

def suma_armonica(n):
    if n <= 0:
        return 0.0
    
    suma = 0.0
    for i in range(1, n + 1):
        suma += 1 / i
    
    return suma

# Ejemplo de uso
n_ejemplo = 5
resultado = suma_armonica(n_ejemplo)
print(f"La suma armónica de los primeros {n_ejemplo} términos es: {resultado}")

# Salida esperada:
# La suma armónica de los primeros 5 términos es: 2.283333333333333


import matplotlib.pyplot as plt

# Generamos los datos
terminos = list(range(1, 101))
valores_suma = [suma_armonica(n) for n in terminos]

# Creamos el gráfico
plt.figure(figsize=(10, 6))
plt.plot(terminos, valores_suma, color='darkorange', linewidth=2)

# Añadimos etiquetas y título
plt.title('Crecimiento de la Suma Armónica', fontsize=16)
plt.xlabel('Número de términos (n)', fontsize=12)
plt.ylabel('Suma Armónica ($H_n$)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

# Mostramos el gráfico
plt.show()