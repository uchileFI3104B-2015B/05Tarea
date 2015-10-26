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

#Main
#Setup

Lx = 10
Ly = 15
h = 0.2
N_pasos_x = int(Lx/h +1)
N_pasos_y = int(Ly/h +1)

v = np.zeros((N_pasos_x, N_pasos_y))
v_next = np.zeros((N_pasos_x, N_pasos_y))
