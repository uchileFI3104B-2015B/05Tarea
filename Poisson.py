# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 19:41:28 2015
Este programa calcula el potencial dentro de una caja de 10x15
que contiene la letra "B" que tiene una carga de 1[C],
usando la ecuación de Poisson.
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def Iteracion(V, V_next, N_pasos_x, N_pasos_y, h, w):
    for i in range(1, N_pasos_x-1):
        for j in range (1, N_pasos_y-1):
            V_next[i, j] = ((1 - w) * V[i, j] +
                            w / 4 * (V[i+1, j] + V[i-1, j]
                                    + V[i, j+1] + V[i, j-1] + 
                                    h**2 * roh(i,j,h))



#Main

#Inicializacion

L_x = 10
L_y = 15
h = 0.2
N_pasos_x = (L_x / h) + 1
N_pasos_y = (L_y / h) + 1

V = np.zeros((N_pasos_x, N_pasos_y))
V_next = np.zeros((N_pasos_x, N_pasos_y))

#Iteracion

Iteracion(V, V_next, N_pasos_x, N_pasos_y, h, w)
contador = 1
while contador < 900 or no_converge(V, V_next, tolerancia=1e-7):
    V = V_next.copy()
    Iteracion(V, V_next, N_pasos_x, N_pasos_y, h, w)
    contador += 1