#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Aquí va la descripcion de mi tarea
'''

import numpy as np
import matplotlib.pyplot as plt


def una_iteracion(V, V_next, N_pasos, h, w):
    pass


def no_ha_convergido(V, V_next, tolerancia):
    pass



# Main

# Setup

Lx = 10
Ly = 15
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
