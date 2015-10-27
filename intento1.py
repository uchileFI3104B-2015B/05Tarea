#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Programa que busca integrar la ecuacion de poisson en 2D
'''
#librerias

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

#funciones estructurales

def r(i, j, Lx, Ly, h):
    x = i* h - Lx/ 2
    y = j* h - Ly/ 2
    dx = 2.5
    dy = 3.5
    l = 1
    rho = 1/11
    if x >= -dx and x <= -dx + l:
        if y >= -dy and y <= dy:
            return rho
    elif x >= l - dx and x <= dx:
        if y >= -dy and y <= -dy +l:
            return rho
    else:
        return 0


#condiciones de borde y/o iniciales

Lx = 10
Ly = 15
N_x = 10
N_y = 15

v = np.zeros((N_x, N_y))
v_s = np.zeros((N_x, N_y))

h = 0.2


#iteracion



#graficos (?)
