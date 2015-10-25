
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

#Punto (0,0) en la esquina inferior izquierda de la grilla
def muestra_V(V):
    print(V[::-1,:])

#Main

#Setup
Lx = 10
Ly = 15
h= 0.2
N_pasosx = (Lx / h) + 1
N_pasosy = (Ly / h) + 1


V = np.zeros((N_pasosy, N_pasosx))
V_next= np.zeros((N_pasosy, N_pasosx))

V[0,0]=1
muestra_V(V)
