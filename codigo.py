'''
Descripcion
'''

import numpy as np
from _future_ import division

#Definimos los parametros para crear la grilla
Lx=10
Ly=15
h=0.2
N_pasos_x = Lx / h + 1
N_pasos_y = Ly / h + 1

#Creamos la grilla
V=np.zeros( ( N_pasos_x , N_pasos_y ) )

#Definimos la funcion rho que asignara un valor de densidad
#a cada punto de la grilla, diferenciando los espacios en
#blanco de los espacios que pertenecen a la letra 'B'
def rho(i, j, h):
    x = i * h - 5
    y = j * h - 7.5
    rho_letra = 1 / 23
    rho_blanco = 0

    if x >= -2.5 and x <= -1.5 and y >= -3.5 and y <= 3.5:
        return rho_letra
    if x >= 1.5 and x <= 2.5 and y >= -3.5 and y <= 3.5:
        return rho_letra
    if y <= 3.5 and x >= 2.5 and x > -1.5 and x < 1.5:
        return rho_letra
    if y <= 0.5 and y >= -0.5 and x > -1.5 and x < 1.5:
        return rho_letra
    if y <= -2.5 and y >= -3.5 and x > -1.5 and x < 1.5:
        return rho_letra
    else:
        return rho_blanco

#Mostramos nuestra grilla
print V
