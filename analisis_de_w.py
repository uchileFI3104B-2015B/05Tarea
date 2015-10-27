#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Programa que busca integrar la ecuacion de poisson en 2D
'''
# librerias

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# funciones estructurales


def r(i, j, Lx, Ly, h):
    x = i * h - Lx / 2
    y = j * h - Ly / 2
    dx = 2.5
    dy = 3.5
    l = 1
    rho = 1 / 11.
    r = 0
    if x >= -dx and x <= -dx + l:
        if y >= -dy and y <= dy:
            r = rho
    elif x >= l - dx and x <= dx:
        if y >= -dy and y <= -dy + l:
            r = rho
    return r


def una_iter(phi, phi_n, p):
    '''
    Da un paso en la iteracion para toda la grilla parte por parte
    '''
    N_x, N_y, Lx, Ly, h, w = p
    N_x = int(N_x)
    N_y = int(N_y)
    for j in range(1, 12):
        'abajo de la linea'
        for i in range(1, N_x - 1):
            'recorre completo'
            phi_n[i, j] = ((1 - w) * phi[i, j] +
                           w / 4 * (phi[i+1, j] + phi_n[i-1, j] +
                                    phi[i, j+1] + phi_n[i, j-1]))

    for j in range(12, 14):
        'en la linea'
        for i in range(1, 11):
            'para el borde antes de la linea'
            phi_n[i, j] = ((1 - w) * phi[i, j] +
                           w / 4 * (phi[i+1, j] + phi_n[i-1, j] +
                                    phi[i, j+1] + phi_n[i, j-1]))
        for i in range(41, N_x - 1):
            'borde despues de la linea'
            phi_n[i, j] = ((1 - w) * phi[i, j] +
                           w / 4 * (phi[i+1, j] + phi_n[i-1, j] +
                                    phi[i, j+1] + phi_n[i, j-1]))
        'esta parte es redundante, pero me sirve para ordenar mis ideas'
        for j in range(12, 13):
            'bajo la linea, usando la condicion -1'
            for i in range(11, 41):
                phi_n[i, j] = ((1 - w) * phi[i, j] +
                               w / 3 * (phi[i+1, j] + phi_n[i-1, j] +
                                        phi_n[i, j-1] +
                                        h ** 2 * r(i, j, Lx, Ly, h) +
                                        h * (-1.)))
        for j in range(13, 14):
            'encima de la linea, usando condicion +1'
            for i in range(11, 41):
                phi_n[i, j] = ((1 - w) * phi[i, j] +
                               w / 3 * (phi[i+1, j] + phi_n[i-1, j] +
                                        phi_n[i, j-1] +
                                        h ** 2 * r(i, j, Lx, Ly, h) +
                                        h * (1.)))
    for j in range(14, 17):
        'sobre la linea y antes del rectangulo de la letra'
        for i in range(1, N_x - 1):
            phi_n[i, j] = ((1 - w) * phi[i, j] +
                           w / 4 * (phi[i+1, j] + phi_n[i-1, j] +
                                    phi[i, j+1] + phi_n[i, j-1]))
    for j in range(17, 58):
        'a la altura del rectangulo'
        for i in range(1, 12):
            'a la derecha'
            phi_n[i, j] = ((1 - w) * phi[i, j] +
                           w / 4 * (phi[i+1, j] + phi_n[i-1, j] +
                                    phi[i, j+1] + phi_n[i, j-1]))
        for i in range(12, 38):
            'dentro'
            phi_n[i, j] = ((1 - w) * phi[i, j] +
                           w / 4 * (phi[i+1, j] + phi_n[i-1, j] +
                                    phi[i, j+1] + phi_n[i, j-1] +
                                    h**2. * r(i, j, Lx, Ly, h)))
        for i in range(38, N_x - 1):
            'a la izq'
            phi_n[i, j] = ((1 - w) * phi[i, j] +
                           w / 4 * (phi[i+1, j] + phi_n[i-1, j] +
                                    phi[i, j+1] + phi_n[i, j-1]))

    for j in range(58, N_y - 1):
        'sobre el rectangulo'
        for i in range(1, N_x - 1):
            phi_n[i, j] = ((1 - w) * phi[i, j] +
                           w / 4 * (phi[i+1, j] + phi_n[i-1, j] +
                                    phi[i, j+1] + phi_n[i, j-1]))


def no_ha_convergido(phi, phi_n, toler=1e-5):
    '''
    ve si la funcion ya ha convergido
    '''
    not_zero = (phi_n != 0)
    res = (phi - phi_n)[not_zero] / phi_n[not_zero]
    max_res = np.max(np.fabs(res))
    if max_res > toler:
        return True
    else:
        return False


def n_relajacion(w=1, N=5000):
    Lx = 10
    Ly = 15
    h = 0.2
    N_x = Lx / h
    N_y = Ly / h
    phi = np.zeros((N_x, N_y))
    phi_s = np.zeros((N_x, N_y))
    'iteracion'
    p = (N_x, N_y, Lx, Ly, h, w)
    'mas practico definir el vector para usar como parametro'
    una_iter(phi, phi_s, p)
    n = 1
    while n < N and no_ha_convergido(phi, phi_s):
        phi = phi_s.copy()
        una_iter(phi, phi_s, p)
        n = n + 1
        print n 'permite ver si el algoritmo esta avanzando o se queda pegado'
    return n


W = [0.8, 1, 1.2, 1.4, 1.6, 1.8, 2]
N = []
for w in W:
    n = n_relajacion(w)
    N.append(n)
print W
print N
fig1 = plt.figure(1)
fig1.clf()
ax1 = fig1.add_subplot(111)
ax1.plot(W, N, 'o')
plt.title('N de relajacion vs $\omega$')
ax1.set_ylabel('N d relajacion')
ax1.set_xlabel('$\omega$')

plt.savefig('N_relajacion.png')
fig1.show()
# [5000, 3727, 2557, 1691, 1011, 442, 5000]
