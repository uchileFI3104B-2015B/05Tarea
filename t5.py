from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


densidad= 1/15
Lx=10
Ly=15
h=0.2

def muestra_phi(phi):
    print(phi[::-1, :])

def rho(i, j, h):
    x=i*h-(Lx/2.) #los x e y están en centímetros, el origen está en el centro de la grilla
    y=j*h-(Ly/2.)
    if (x>=-2.5 and x<=2.5) and (y>=2.5 and y<=3.5): #arriba C
        return densidad

    elif (x>=-2.5 and x<=2.5) and (y>=-3.5 and y<=-2.5): #parte baja de C
        return densidad
    elif (x<=-1.5 and x>=-2.5) and (y>=-2.5 and y<=2.5 ) #palo del medio
        return densidad
    else:
        return 0
