'''
Descripcion
'''
from __future__ import division
import numpy as np

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

#Definimos la funcion 'una_iteracion'
def una_iteracion(V, V_next, N_pasos_x, N_pasos_y, h, w):
    for i in range(1, int(N_pasos_x) - 1):
        #Separamos la grilla para aislar el lugar con condicion derivativa

        #Bajo la condicion derivativa
        for j in range(1, 12):
            V_next[i, j] = ((1 - w) * V[i, j] + w / 4 * (V[i+1, j] + V_next[i-1, j]
                            + V[i, j+1] + V_next[i, j-1] + h**2 * rho(i, j, h)))

        #sobre la condicion derivativa
        for j in range(14, int(N_pasos_y) - 1):
            V_next[i, j] = ((1 - w) * V[i, j] + w / 4 * (V[i+1, j] + V_next[i-1, j]
                            + V[i, j+1] + V_next[i, j-1] + h**2 * rho(i, j, h)))


    for j in range(12,14):

        #A la izquierda de la condicion derivativa
        for i in range(1,11):
            V_next[i, j] = ((1 - w) * V[i, j] + w / 4 * (V[i+1, j] + V_next[i-1, j]
                            + V[i, j+1] + V_next[i, j-1] + h**2 * rho(i, j, h)))

        #A la derecha de la condicion derivativa
        for i in range(41,int(N_pasos_x)-1):
            V_next[i, j] = ((1 - w) * V[i, j] + w / 4 * (V[i+1, j] + V_next[i-1, j]
                            + V[i, j+1] + V_next[i, j-1] + h**2 * rho(i, j, h)))

    #Ahora iteramos dentro de la condicion derivativa
    for i in range(11,41):
        #Bajo la condicion derivativa -1
        for j in range(12,13):
            V_next[i,j] =  ((1 - w) * V[i, j] + w / 3 * (V[i+1, j] + V_next[i-1, j]
                            + V[i, j-1] + h**2 * rho(i, j, h) + h*(-1.)))

        #Sobre la condicion derivativa +1
        for j in range(13,14):
            V_next[i,j] =  ((1 - w) * V[i, j] + w / 3 * (V[i+1, j] + V_next[i-1, j]
                            + V[i, j-1] + h**2 * rho(i, j, h) + h*(1.)))


#Main

#Setup
Lx=10
Ly=15
h=0.2
N_pasos_x = Lx / h + 1
N_pasos_y = Ly / h + 1
w=1
#Creamos la grilla
V=np.zeros( ( N_pasos_x , N_pasos_y ) )
V_next=np.zeros( ( N_pasos_x , N_pasos_y ) )

#Mostramos nuestra grilla
print V_next
