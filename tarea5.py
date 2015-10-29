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



def no_ha_convergido(V, Vnext, tolerancia=1e-3):



