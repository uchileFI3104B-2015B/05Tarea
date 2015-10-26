
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


#Punto (0,0) en la esquina inferior izquierda de la grilla
def muestra_V(V):
    print(V[::-1,:])

def rho(i, j, h):
    x = i * h - 5
    y = j * h - 7.5
    rho_letra = 1 / 15
    rho_blanco = 0

    if y>=2.5 and y<=3.5 and x>=-2.5 and x<=2.5:
        return rho_letra
    if y<=-2.5 and y>=-3.5 and x>=-2.5 and x<=2.5:
        return rho_letra
    if y>=-2.5 and y<=2.5 and x>=-2.5 and x<=-1.5:
        return rho_letra
    else:
        return rho_blanco


#Main

#Setup
Lx = 10
Ly = 15
h= 0.2
N_pasosx = (Lx / h) + 1
N_pasosy = (Ly / h) + 1
w=1.0


V = np.zeros((N_pasosx, N_pasosy))
V_next= np.zeros((N_pasosx, N_pasosy))


#Una iteracion
