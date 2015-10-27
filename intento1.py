#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Programa que busca integrar la ecuacion de poisson en 2D
'''
#librerias

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

#funciones estructurales

def r(i, j, Lx, Ly, h):
    x = i* h - Lx/ 2
    y = j* h - Ly/ 2
    dx = 2.5
    dy = 3.5
    l = 1
    rho = 1/11.
    r = 0
    if x >= -dx and x <= -dx + l:
        if y >= -dy and y <= dy:
            r = rho
    elif x >= l - dx and x <= dx:
        if y >= -dy and y <= -dy +l:
            r = rho
    return r


'''
def paso_sin_carga(phi, phi_n, N_x, N_y):
    'solo la iteracion son considerar el valor de la densidad'
    N_x = int(N_x)
    N_y = int(N_y)
    for i in range(1, N_x - 1):
        for j in range(1, N_y - 1):
            phi_n[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_n[i-1, j] +
                                       phi[i, j+1] + phi_n[i, j-1] ))


def paso_con_carga(phi, phi_n, p, nx_i, ny_i, nx_f, ny_f):
    'solo la iteracion en las zonas con carga'
    N_x, N_y, Lx, Ly, h, w = p
    N_x = int(N_x)
    N_y = int(N_y)
    for i in range(1, N_x - 1):
        for j in range(1, N_y - 1):
            phi_n[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_n[i-1, j] +
                                       phi[i, j+1] + phi_n[i, j-1] +
                                       h**2. * r(i, j, Lx, Ly, h)))
'''



def una_iter(phi, phi_n, p): # = N_x, N_y, Lx, Ly, h, w = 1.
    '''
    Da un paso en la iteracion para toda la grilla
    '''
    N_x, N_y, Lx, Ly, h, w = p
    N_x = int(N_x)
    N_y = int(N_y)
    for i in range(1, N_x - 1):
        for j in range(1, N_y - 1):
            phi_n[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_n[i-1, j] +
                                       phi[i, j+1] + phi_n[i, j-1] +
                                       h**2. * r(i, j, Lx, Ly, h)))



    pass


def no_ha_convergido(phi, phi_n, toler = 1e-5):
    '''
    ve si la funcion ya ha convergido
    '''
    not_zero = (phi_n != 0)
    res = (phi - phi_n)[not_zero]/ phi_n[not_zero]
    max_res = np.max(np.fabs(res))
    if max_res > toler:
        return True
    else:
        return False
#    pass


#condiciones de borde y/o iniciales

Lx = 10
Ly = 15
h = 0.2
w = 1
N_x = Lx/ h
N_y = Ly/ h


phi = np.zeros((N_x, N_y))
phi_s = np.zeros((N_x, N_y))


#iteracion

p= (N_x, N_y, Lx, Ly, h, w )
una_iter(phi, phi_s, p)
n = 1
Nf = 100
while n < Nf and no_ha_convergido(phi, phi_s):
    phi = phi_s.copy()
    una_iter(phi, phi_s, p)
    n = n + 1
    print n






#graficos (?)
print("contador = {}".format(n))
'''
fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-Lx/2, Lx, N_x)
y = np.linspace(-Ly/2, Ly, N_y)

X, Y = np.meshgrid(x, y)

ax.plot_surface(X, Y, phi_s, rstride=1, cstride=1)
fig.show()
'''
fig2 = plt.figure(2)
fig2.clf()
ax2 = fig2.add_subplot(111)
ax2.imshow(phi_s, origin='bottom', interpolation='nearest')
ax2.contour(phi_s, origin='lower')
fig2.show()

plt.draw()
