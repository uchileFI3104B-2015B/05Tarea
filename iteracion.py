#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from caja import Caja

def sobre_relajacion(C, w):
    V_anterior = C.get_potencial()
    C.relaja(w,1)
    V_actual = C.get_potencial()
    chi2 = np.sum(np.power(V_actual - V_anterior, 2))
    N_pasos = 1
    print chi2
    while chi2 > 0.001:
        pasos = np.floor(10 * np.power(chi2, 0.1) + 1)
        C.relaja(w, pasos)
        V_anterior = C.get_potencial()
        C.relaja(w, 1)
        V_actual = C.get_potencial()
        N_pasos += pasos + 1
        chi2ant = chi2
        chi2 = np.sum(np.power(V_actual - V_anterior, 2))
        print chi2
    return N_pasos

def experimento_w(C,arreglo_w):
    N_w = []
    V_w = []
    for w in arreglo_w:
        C.resetea_potencial()
        print w
        N_w.append(sobre_relajacion(C, w))
        V_w.append(C.get_potencial())
    return N_w, V_w

C = Caja()
C.agregar_letra_B()
C.agregar_linea_horizontal()
rango_w = np.linspace(0.2, 1.8, 9)
n_iter, V_iter = experimento_w(C, rango_w)

A = C.get_carga()
plt.figure(1)
plt.imshow(A, origin='bottom', interpolation='nearest', cmap = 'gray')
plt.colorbar()
plt.savefig('carga.eps')

y = C.reticulado * np.array(range(C.Ny))
for n in range(9):
    V = V_iter[n]
    V_y = np.zeros(C.Ny)
    for k in range(C.Ny):
        V_y[k] = V[k][20]
    fig = plt.figure(2*n+2)
    ax = fig.add_subplot(111)
    ax.plot(y,V_y)
    ax.set_aspect('equal')
    plt.savefig('perfil'+str(int(10 * rango_w[n])+'.eps')
    plt.figure(2*n+3)
    plt.imshow(V, origin='bottom', interpolation='nearest', vmin=-3, vmax=3)
    plt.colorbar()
    plt.savefig('potencial'+str(int(10 * rango_w[n]))+'.eps')
