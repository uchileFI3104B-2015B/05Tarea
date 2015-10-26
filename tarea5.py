'''
Este script...
'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def muestra_v(v):
    print(v[::-1, :])


#Main
#Setup

Lx = 10
Ly = 15
h = 0.2
N_pasos_x = int(Lx/h +1)
N_pasos_y = int(Ly/h +1)

v = np.zeros((N_pasos_x, N_pasos_y))
v_next = np.zeros((N_pasos_x, N_pasos_y))
