from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def muestra_V(V):
    print(V[::-1, :])


def densidad_letra(i, j, h):
    '''Se busca donde esta la letra "L", asignandole el valor de su densidad'''
    x = i*h - 5
    y = j*h - 7.5
    letra = 1/11

    if y <= -2.5 and y >= -3.5 and x >= -3. and x <= 3.:
        return letra
    if y >= -2.5 and y <= 5.5 and x >= -3. and x <= -2.:
        return letra
    else:
        return 0


def una_iteracion(V, Vnext, Nx_pasos, Ny_pasos, h, w=1.):
    for i in range(1, int(Nx_pasos) - 1):
        for j in range(1, 13):  #Bajo linea
            Vnext[i, j] = ((1 - w)*V[i, j] + w/4*(V[i + 1, j] +
                            Vnext[i - 1, j] + V[i, j + 1] + Vnext[i, j - 1] +
                                 h**2*densidad_letra(i, j, h)))
        for j in range(15, int(Ny_pasos) - 1):  #Sobre linea
            Vnext[i, j] = ((1 - w)*V[i, j] + w/4*(V[i + 1, j] +
                            Vnext[i - 1, j] + V[i, j + 1] + Vnext[i, j - 1] +
                                 h**2*densidad_letra(i, j, h)))
    for j in range(13, 15):
        for i in range(1, 12):  #Izq. linea
            Vnext[i, j] = ((1 - w)*V[i, j] + w/4*(V[i + 1, j] +
                            Vnext[i - 1, j] + V[i, j + 1] + Vnext[i, j - 1] +
                                     h**2*densidad_letra(i, j, h)))
        for i in range(42, int(Nx_pasos) - 1):  #Der. linea
            Vnext[i, j] = ((1 - w)*V[i, j] + (w/4)*(V[i + 1, j] +
                            Vnext[i - 1, j] + V[i, j + 1] + Vnext[i, j - 1] +
                                     h**2*densidad_letra(i, j, h)))

    for i in range(12, 42):  #condicion derivada
        for j in range(13, 14):  #puntos debajo linea
            Vnext[i, j] = ((1 - w)*V[i, j] + w/3*(V[i + 1, j] +
                            Vnext[i - 1, j] + Vnext[i, j - 1] +
                                     h**2*densidad_letra(i, j, h) + h*(-1.)))
        for j in range(14, 15):  #puntos sobre linea
            Vnext[i, j] = ((1 - w)*V[i, j] + w/3*(V[i + 1, j] +
                            Vnext[i - 1, j] + Vnext[i, j - 1] +
                                     h**2*densidad_letra(i, j, h) + h*1.))


def no_ha_convergido(V, Vnext, tolerancia=1e-3):



