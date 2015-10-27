#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from caja import Caja


def convergencia(C,arreglo_w):
    C.resetea_potencial()
    C.relaja(1,1000)
    V_obj = C.get_potencial()
    N_w = []
    V_w = []
    for w in arreglo_w:
        print "w =", w
        C.resetea_potencial()
        chi2 = 50
        n = 0
        while chi2 > 15 and n < 10000:
            paso = np.ceil(chi2/100)
            C.relaja(w, paso)
            n += paso
            chi2 = np.sum(np.power(C.get_potencial() - V_obj,2))
        if n >= 1000:
            N_w.append(-1)
            print "No converge después de 10000 iteraciones"
        else:
            N_w.append(n)
            print "Converge después de", n, "iteraciones"
        V_w.append(C.get_potencial())
        print ""
    return N_w, V_w

C = Caja()
C.agregar_letra_B()
C.agregar_linea_horizontal()
rango_w = np.linspace(0.2, 1.8, 9)
n_iter, V_iter = convergencia(C, rango_w)

A = C.get_carga()
fig = plt.figure(1)
plt.clf()
plt.imshow(A, origin='bottom', interpolation='nearest', cmap = 'gray',
extent= [-5,5,-7.5,7.5])
plt.colorbar()
plt.title('Densidad de carga en el rect'u'á''ngulo')
plt.savefig('carga.eps')

plt.figure(2)
plt.clf()
plt.plot(rango_w, n_iter)


y = C.reticulado * np.array(range(C.Ny))

plt.clf()
for n in range(9):
    V = V_iter[n]
    V_y = np.zeros(C.Ny)
    for k in range(C.Ny):
        V_y[k] = V[k][20]

    fig = plt.figure(2*n+3)
    ax = fig.add_subplot(111)
    ax.plot(y,V_y)
    ax.set_aspect('equal')
    plt.savefig('perfil'+str(int(10 * rango_w[n]))+'.eps')

    plt.figure(2*n+4)
    plt.imshow(V, origin='bottom', interpolation='nearest') #, vmin=-3, vmax=3)
    plt.colorbar()
    plt.savefig('potencial'+str(int(10 * rango_w[n]))+'.eps')
