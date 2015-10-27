#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Aquí va la descripcion de mi tarea
'''
densdad = 1. / 20.
Lx = 10
Ly = 15

import numpy as np
import matplotlib.pyplot as plt


def rho(i, j, h):
    x = i * h - Lx / 2. #La resta es para dejar el eje al centro
    y = j * h - Ly / 2.
    if (x>=-2.5 and x <= 2.5) and (y>=-3.5 and y <= 3.5):
        #Esta condicion es para entrar a la caja
        if (x >= -2.5 and  x <= -1.5) or (x >= 1.5 and x <= 2.5):
            #Lineas a los lados de M
            return densidad

        elif (x>=-1.5 and x <= -0.5) and (y>=0.5 and y >=2.5):
            #Barrita a la izquierda
            return densidad

        elif (x>=0.5 and x <= 1.5) and (y>=0.5 and y >=2.5):
            #Barrita a la derecha
            return densidad

        elif (x >= -0.5 and x <= 0.5) and (y >= -0.5 and y <= 1.5):
            #Barrita al medio
            return densidad

        else:
            return 0 #Dentro de la caja pero no es la letra M

    else:
        return 0 #Fuera de la caja

def una_iteracion(V, V_next, N_pasos, h, w):
    pass


def no_ha_convergido(V, V_next, tolerancia):
    pass



# Main

# Setup


h = 0.2
N_steps_x = Lx / h
N_steps_y = Ly / h

V = np.zeros((Lx / h, Ly / h))
V_next = np.zeros((Lx / h, Ly / h))
w = 1

# Matriz que define rho
rho = np.zeros((Lx / h, Ly / h))







una_iteracion(V, V_next, N_pasos_x, N_pasos_y, h, w)
counter = 1
while counter < 800 and no_ha_convergido(V, V_next, tolerancia=1e-7):
    V = V_next.copy()
    una_iteracion(V, V_next, N_pasos_x, N_pasos_y, h, w)
    counter += 1
