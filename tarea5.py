'''
Este script...
'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def muestra_v(v):
    print(v[::-1, :])


def rho(i, j, h):
    x= i * h - 5
    y= j * h - 7.5
    if y>=2.5 and y<=3.5 and x>=-2.5 and x<=2.5:
        return 1./15
    if y>=1 and y<=2.5 and x>=-2.5 and x<=-1.5:
        return 1./15
    if y>=0 and y<=1 and x>=-2.5 and x<=2.5:
        return 1./15
    if y>=-3.5 and y<=0 and x>=-2.5 and x<=-1.5:
        return 1./15
    else:
        return 0


# Se debe separar la iteracion en distintos segmentos:
#hay una ec para los puntos lejanos a la linea neumann
#hay otra para los inmediatamente vecinos a la linea neumann
#y finalmente otra para los ptos de la linea neumann en si.
#linea neumann y=-5.5 entre x=[-3,3]
def una_iteracion(v, v_next, N_pasos_x, N_pasos_y, h=0.2, w=1.):
    for i in range(1, N_pasos_x-1):
        #arriba
        for j in range(1, 11):
            v_next[i, j] = ((1 - w) * v[i, j] +
                              w / 4 * (v[i+1, j] + v_next[i-1, j] +
                                       v[i, j+1] + v_next[i, j-1] +
                                       h**2 * rho(i, j, h)))
        #abajo
        for j in range(14, N_pasos_y-1):
            v_next[i, j] = ((1 - w) * v[i, j] +
                              w / 4 * (v[i+1, j] + v_next[i-1, j] +
                                       v[i, j+1] + v_next[i, j-1] +
                                       h**2 * rho(i, j, h)))

    for j in range(11,14):
        #izq
        for i in range(1,10):
            v_next[i, j] = ((1 - w) * v[i, j] +
                              w / 4 * (v[i+1, j] + v_next[i-1, j] +
                                       v[i, j+1] + v_next[i, j-1] +
                                       h**2 * rho(i, j, h)))
        #der
        for i in range(41,N_pasos_x-1):
            v_next[i, j] = ((1 - w) * v[i, j] +
                          w / 4 * (v[i+1, j] + v_next[i-1, j] +
                                   v[i, j+1] + v_next[i, j-1] +
                                   h**2 * rho(i, j, h)))



    #vecinos, cuando v_next o v???
    for i in range(10,41):
        for j in range(11,12):#abajo
            v_next[i,j] =  ((1 - w) * v[i, j] +
                          w / 3 * (v[i+1, j] + v_next[i-1, j] +
                                   v[i, j-1] + h**2 * rho(i, j, h) + h*(-1.)))
        for j in range(13,14):#arriba
            v_next[i,j] =  ((1 - w) * v[i, j] +
                          w / 3 * (v[i+1, j] + v_next[i-1, j] +
                                   v[i, j-1] + h**2 * rho(i, j, h) + h*(1.)))
    #en la linea neumann
    for j in range(12,13):
        for i in range(10,41):
            v_next[i,j] = v_next[i,j-1]+h*(1.)
#Main
#Setup

Lx = 10
Ly = 15
h = 0.2
N_pasos_x = int(Lx/h +1)
N_pasos_y = int(Ly/h +1)

v = np.zeros((N_pasos_x, N_pasos_y))
v_next = np.zeros((N_pasos_x, N_pasos_y))
