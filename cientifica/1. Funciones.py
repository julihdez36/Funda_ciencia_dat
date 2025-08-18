 # Funciones
# Definamos una función que convierte de coordenadas polares a cartesianas

from math import sqrt, atan

def CartesianaAPolares(x,y): # recibe coordenadas cartesianas
    r = sqrt(x**2 + y**2) # longitud r
    t = atan(y/x) # ángulo con la inversa de la tangente
    return r,t

x, y = 2.0, 4.0
radio, theta = CartesianaAPolares(x,y)

print(f'x = {x}, y = {y}, r = {radio}, theta = {theta}')
