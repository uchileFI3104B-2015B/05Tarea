#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


class circuito(object):

    def __init__(self,ancho,largo,paso=0.2):
        N_pasos_x=int(ancho/paso)+1
        N_pasos_y=int(largo/paso)+1
        self.x=np.linspace(-ancho/2,ancho/2,N_pasos_x)
        self.y=np.linspace(-largo/2,largo/2,N_pasos_y)
        self.v=np.zeros((x, y))
        self.dv=np.zeros((x, y))
        self.densidad_carga=np.zeros((x, y))

    def hay_letra(self,ancho,largo):
        '''
        verifica si dentro del recuadro se encuentra parte de la letra
        '''
        pass

#--------------------Ahora se calcula la solucion del sistema------------------#

def iteracion_sobrerelajacion(V,V_next,DV,N_pasos_x,N_pasos_y,h,rho,w=1.2):
    for i in range(2, N_pasos_x-2):
        for j in range(2, N_pasos_y-2):
            V_next[i, j] = ((1 - w) * V[i, j] +
                              w / 4 * (V[i+1, j] + V_next[i-1, j] +
                                       V[i, j+1] + V_next[i, j-1] +
                                       h**2 * rho[i, j]))

    for i in range(0,N_pasos_y):

        #bordes en la direccion y#
         V_next[i,N_pasos_y] =V_next[i,N_pasos_y-1]+h*DVy[i,N_pasos_y]
         V_next[i,0] =V_next[i,1]+h*DV[i,0]

         #lineas antes de los bordes
         V_next[i,N_pasos_y-1] = ((1 - w) * V[i, N_pasos_y-1] +
                                   w / 4 * (V[i+1, N_pasos_y-1] +
                                            V_next[i-1, N_pasos_y-1] +
                                            V[i, N_pasos_y] + V_next[i, N_pasos_y-2] +
                                            h**2 * rho[i, N_pasos_y-1] +
                                            h * DV[i,N_pasos_y-1]))

         V_next[i,1] = ((1 - w) * V[i, 1] +
                         w / 4 * (V[i+1, 1] + V_next[i-1, 1] +
                                            V[i, 2] + V_next[i, 0] +
                                            h**2 * rho[i, 1] +
                                            h * DVy[i,1]))


    for j in range(0,N_pasos_y):

        #bordes en la direccion x#
         V_next[N_pasos_x,j] =V_next[N_pasos_x-1,j]+h*DV[N_pasos_x,j]
         V_next[j,0] =V_next[1,j]+h*DV[j,0]

         #lineas antes de los bordes
         V_next[N_pasos_x-1,j] = ((1 - w) * V[N_pasos_x-1,j] +
                                   w / 4 * (V[N_pasos_x-1, j+1] +
                                            V_next[N_pasos_x-1,j-1] +
                                            V[N_pasos_x,j] + V_next[N_pasos_x-2,j] +
                                            h**2 * rho[N_pasos_x-1,j] +
                                            h * DVy[N_pasos_X-1,j]))

         V_next[1,j] = ((1 - w) * V[1,j] +
                         w / 4 * (V[1,j + 1] + V_next[1, j-1] +
                                            V[2, j] + V_next[0, j] +
                                            h**2 * rho[1, j] +
                                            h * DVy[1, j]))


h=0.2
c=circuito(10,15,h)
V_next=np.zeros(c.N_pasos_x,c.N_pasos_y)

#iteracion#
iteracion_sobrerelajacion(c.v(),V_next,v.N_pasos_x(),v.N_pasos_y(),h,w=1.2)
conuter=1
while counter < 800 and no_ha_convergido(c.v(), V_next, tolerancia=1e-7):
    n.v() = v_next.copy()
    iteracion_sobrerelajacion(c.v(),V_next,v.N_pasos_x(),v.N_pasos_y(),h,w=1.2))
    counter += 1
