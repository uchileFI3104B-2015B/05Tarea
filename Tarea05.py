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
        self.dvx=np.zeros((x, y))
        self.dvy=np.zeros((x, y))
        self.densidad_carga=np.zeros((x, y))

    def hay_letra(self):
        pass

#--------------------Ahora se calcula la solucion del sistema------------------#

def iteracion_sobrerelajacion(V,V_next,N_pasos_x,N_pasos_y,w=1.2):
    pass
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
