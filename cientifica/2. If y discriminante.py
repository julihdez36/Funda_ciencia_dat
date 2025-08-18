# Condicional if para el calculo del discriminante

# --------------------------------------------------------
# Condicional if

'''
Imaginemos que queremos evaluar los coeficientes de una ecuación cuadrática.
Queremos saber si ésta tiene raices reales.

Para ello, debemos calcular el discriminante: d = b^2 - 4ac.
Si el discriminante es > 0, tenemos dos soluciones reales.
Si el discriminante < 0, no tenemos soluciones reales
Si el disceiminante = 0, obtenemos una solución real
'''

a = -1.0
b = 1.0
c = -3.2

d = b**2 - 4*a*c

if d >= 0:
    print('La ecuación tiene raices reales')
else: print('La ecuación tiene solución compleja')

# una forma de abreviar el if es a través del operador teniario

k= a if d>=0 else b

# Definamos la función completa

def discriminante(a,b,c):
    d = b**2 - 4*a*c
    if d == 0:
        print('La ecuación tienen una solución real, una raíz doble')
    elif d > 0:
        print('La ecuación tiene raices reales')
    else: print('La ecuación tiene solución compleja')






