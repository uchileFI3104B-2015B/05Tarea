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


#Main

#Inicializacion

Lx = 10
Ly = 15
h = 0.2
N_pasos_x = (Lx / h) + 1
N_pasos_y = (Ly / h) + 1

V = np.zeros((N_pasos_x, N_pasos_y))
V_next = np.zeros((N_pasos_x, N_pasos_y))

