
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
h= 1
N_pasosx = (Lx / h) + 1
N_pasosy = (Ly / h) + 1
w=1.0
rho_letra = 1 / 15
rho_blanco = 0


V = np.zeros((N_pasosx, N_pasosy))
V_next= np.zeros((N_pasosx, N_pasosy))


#Una iteracion
for i in range(1, int(N_pasosx) - 1):
    for j in range(1, int(N_pasosy) - 1):
        V[i, j] = (1 - w) * V[i, j] + w / 4 * (V[i+1,j] + V[i-1, j] + V[i, j+1] + V[i, j-1] + h**2 * rho_letra)

muestra_V(V)
