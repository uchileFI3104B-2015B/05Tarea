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
import pdb

def crear_caja(x, y, h):
    '''Recibe las dimensiones de la caja  y el tamaño del reticulado
     y la inicia en puros ceros '''
    ancho_efectivo = x / h + 1
    alto_efectivo = y / h + 1
    caja = np.zeros((ancho_efectivo, alto_efectivo))

    return caja

def poner_condiciones_borde(caja):
    '''conecta a tierra el perímetro de la caja, la segunda iteración
    (bordes laterales) se itera desde borde+1, hasta borde para evitar pasar
    2 veces por las esquinas'''
    borde_inferior = np.array([np.array([-5, -7.5]), np.array([5, -7.5])])
    borde_superior = np.array([np.array([-5, 7.5]), np.array([5, 7.5])])
    borde_inferior[0] = transformar(borde_inferior[0])
    borde_inferior[1] = transformar(borde_inferior[1])
    borde_superior[0] = transformar(borde_superior[0])
    borde_superior[1] = transformar(borde_superior[1])
    for i in range(int(borde_inferior[0][0]), int(borde_inferior[1][0]) + 1):
        caja[i, borde_inferior[0][1]] = 0
        caja[i, borde_superior[0][1]] = 0
    for i in range(int(borde_inferior[0][1])+1, int(borde_superior[0][1])):
        caja[borde_inferior[0][0], i] = 0
        caja[borde_superior[1][0], i] = 0
    return caja
    


def dentro_letra_B(x, y, h):
    

def rho(x, y, h):
    if dentro_letra_B(x, y, h):
        return 1 / 20
    else:
        return 0

def Iteracion(V, V_next, N_pasos_x, N_pasos_y, h, w):
    for i in range(1, N_pasos_x-1):
        for j in range (1, N_pasos_y-1):
            V_next[i, j] = ((1 - w) * V[i, j] +
                            w / 4 * (V[i+1, j] + V[i-1, j]
                                    + V[i, j+1] + V[i, j-1] + 
                                    h**2 * rho(i, j, h)))

def no_converge(V, V_next, tolerancia=1e-7):
    not_zero = (V_next != 0)
    diff_relativa = (V - V_next)[not_zero] / V_next[not_zero]
    max_diff = np.max(np.fabs(diff_relativa))
    if max_diff > tolerancia:
        return True
    else:
        return False

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
    
