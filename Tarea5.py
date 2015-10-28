# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:37:03 2015

@author: splatt
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def muestra_phi(phi):
    print(phi[::-1, :])

def en_letra(i,j,Letra):
    if Letra.count((i,j))!=0:
        return True
    else:
        return False

def en_linea(i,j, Linea):
    if Linea.count((i,j))!=0:
        return True
    else:
        return False

def arriba_linea(i,j, arLinea):
    if arLinea.count((i,j))!=0:
        return True
    else:
        return False
        
def abajo_linea(i,j, abLinea):
    if abLinea.count((i,j))!=0:
        return True
    else:
        return False
    
def una_iteracion(V, V_next, Nx_pasos, Ny_pasos, h, Letra,Ab_linea,Ar_linea,w=1.):
    for i in range(1, Nx_pasos-1):
            for j in range(1, Ny_pasos-1):
                if arriba_linea():
                    V_next[i, j] = ((1 - w) * V[i, j] +
                                  w / 3 * (V[i+1, j] + V_next[i-1, j] +
                                           V[i, j-1] + h))
                
                elif abajo_linea():
                    V_next[i, j] = ((1 - w) * V[i, j] +
                                  w / 3 * (V[i+1, j] + V_next[i-1, j] +
                                           V[i, j-1] - h))
        
                elif en_letra(i,j,Letra):
                    V_next[i, j] = ((1 - w) * V[i, j] +
                                  w / 4 * (V[i+1, j] + V_next[i-1, j] +
                                           V[i, j+1] + V_next[i, j-1] -
                                           1./20.))
                else:
                    V_next[i, j] = ((1 - w) * V[i, j] +
                                  w / 4 * (V[i+1, j] + V_next[i-1, j] +
                                           V[i, j+1] + V_next[i, j-1]))


def no_ha_convergido(V, V_next, tolerancia=1e-5):
    not_zero = (V_next != 0)
    diff_relativa = (V - V_next)[not_zero] / V_next[not_zero]
    max_diff = np.max(np.fabs(diff_relativa))
    if max_diff > tolerancia:
        return True
    else:
        return False


# Main

# Setup

Lx = 10.
Ly = 15.
h=0.2
Nx_pasos = int(Lx/h+1)
Ny_pasos = int(Ly/h+1)

V = np.zeros((Nx_pasos, Ny_pasos))
V_next = np.zeros((Nx_pasos, Ny_pasos))

#Crear letra M

LetraM=[]
for X in range(13,18):
    for Y in range(21,56):
        LetraM.append((X,Y))
for X in range(18,23):
    for Y in range(41,51):
        LetraM.append((X,Y))        
for X in range(23,28):
    for Y in range(36,46):
        LetraM.append((X,Y))
for X in range(28,33):
    for Y in range(41,51):
        LetraM.append((X,Y))
for X in range(33,38):
    for Y in range(21,56):
        LetraM.append((X,Y))

#Densidad de carga=
#RHO=1./20./(h**2)

#Crear linea

Abajo_Linea=[]
for X in range(8,43):
    Abajo_Linea.append((X,13))
    
Arriba_Linea=[]
for X in range(8,43):
    Arriba_Linea.append((X,14))

# iteracion
una_iteracion(V, V_next, Nx_pasos, Ny_pasos, h, LetraM,Abajo_Linea,Arriba_Linea,w=1.)
counter = 1
while counter < 800 and no_ha_convergido(V, V_next, tolerancia=1e-7):
    V = V_next.copy()
    una_iteracion(V, V_next, Nx_pasos, Ny_pasos, h, LetraM,Abajo_Linea,Arriba_Linea, w=1.)
    counter += 1

print("counter = {}".format(counter))

fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-1, 1, Nx_pasos)
y = np.linspace(-1, 1, Ny_pasos)

X, Y = np.meshgrid(x, y)

ax.plot_surface(X, Y, V_next, rstride=1, cstride=1)
fig.show()

fig2 = plt.figure(2)
fig2.clf()
ax2 = fig2.add_subplot(111)
ax2.imshow(V_next, origin='bottom', interpolation='nearest')
ax2.contour(V_next, origin='lower')
fig2.show()

plt.draw()