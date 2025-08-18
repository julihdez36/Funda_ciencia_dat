# Formula de Leibniz para el cálculo de pi
# Lo compararemos con el producto de Wallis


# Serie de Leibniz

def approachLeibniz(n):
    serie = []
    for i in range(n):
        a = (-1)** i
        b = 2*i + 1
        serie.append(a/b)
    return 4 * sum(serie)

approachLeibniz(100000)

# Serie de Wallis
import math

def approachWallis(n):
    serie = []
    for i in range(1,n+1):
        a = (2*i) / (2*i-1) 
        b = (2*i) / (2*i+1)
        serie.append(a*b)
    return 2 * math.prod(serie)

approachWallis(1000)
approachLeibniz(1000)

print('Serie \t \t n = 100 \t n=1000 \t n=10000')
print('Leibniz \t %f \t %f \t %f'%(approachLeibniz(100),approachLeibniz(1000),approachLeibniz(10000)))
print('Wallis \t \t %f \t %f \t %f'%(approachWallis(100),approachWallis(1000),approachWallis(10000)))

# Qué serie converge mas rápido?

import numpy as np
import matplotlib.pyplot as plt

n_list = np.linspace(1,1000,1000, dtype = int) # generalista 1-100 dividida en 1000

leibniz_list = []
wallis_list = []

for i in n_list:
    leibniz_list.append(approachLeibniz(i))
    wallis_list.append(approachWallis(i))
    
plt.plot(n_list, leibniz_list, 'o-', label = 'Leibniz')    
plt.plot(n_list, wallis_list, 'o-', label = 'Wallis') 
plt.legend()
plt.xlabel('n')
plt.ylabel('Valor de pi')
plt.grid(ls = 'dashed')


