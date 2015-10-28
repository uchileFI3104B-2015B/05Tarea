#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


densidad = 1/15
Lx = 10
Ly = 15
h = 0.2
N_pasos_x = int(Lx/h + 1)
N_pasos_y = int(Ly/h + 1)


def muestra_phi(phi):
    print(phi[::-1, :])


def rho(i, j, h):

    x = i * h - (Lx / 2.)
    y = j * h - (Ly / 2.)

    if (x >= -2.5 and x <= 2.5) and (y >= 2.5 and y <= 3.5):  # arriba C
        return densidad

    elif (x >= -2.5 and x <= 2.5) and (y >= -3.5 and y <= -2.5):  # baja de C
        return densidad

    elif (x <= -1.5 and x >= -2.5) and (y >= -2.5 and y <= 2.5):  # medio
        return densidad
    else:
        return 0


def una_iteracion(phi, phi_next, N_pasos_x, N_pasos_y, h=0.2, w=1.):

    ''' esta funcion lo que realiza es dividir la caja y calcular el potencial
    segun
    las condiciones dadas previamente

    condiciones cercano a la linea bajo la letra
    primero: calculamos el tramo bajo la linea la linea esta en -5.5
    que en nuestra grilla seria posicion 10 y sobre la linea, luego
    al lado de la linea y finalmente las condiciones derivativas o como se
    escriba jiji'''

    for i in range(1, N_pasos_x - 1):

        for j in range(1, 10):  # recorremos bajo la linea
            phi_next[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_next[i-1, j] +
                                       phi[i, j+1] + phi_next[i, j-1] +
                                       h**2 * rho(i, j, h)))

        for j in range(12, N_pasos_y-1):  # recorremos sobre la linea
            phi_next[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_next[i-1, j] +
                                       phi[i, j+1] + phi_next[i, j-1] +
                                       h**2 * rho(i, j, h)))

        '''alrededor de la linea costado izquiedo y costado derecho :C '''

    for j in range(10, 12):

        for i in range(1, 11):  # izquierda
            phi_next[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_next[i-1, j] +
                                       phi[i, j+1] + phi_next[i, j-1] +
                                       h**2 * rho(i, j, h)))
        for i in range(41, N_pasos_x-1):
            phi_next[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_next[i-1, j] +
                                       phi[i, j+1] + phi_next[i, j-1] +
                                       h**2 * rho(i, j, h)))

        '''en la linea'''

    for i in range(10, 41):
        # deajo de la linea

        for j in range(10, 11):
            phi_next[i, j] = ((1 - w) * phi[i, j] +
                              w / 3 * (phi[i+1, j] + phi_next[i-1, j] +
                                       phi_next[i, j-1] + h**2 * rho(i, j, h) +
                                       h*(-1.)))
        # sobre la linea
        for j in range(11, 12):
            phi_next[i, j] = ((1 - w) * phi[i, j] +
                              w / 3 * (phi[i+1, j] + phi_next[i-1, j] +
                                       phi_next[i, j-1] + h**2 * rho(i, j, h) +
                                       h*(1.)))


def no_ha_convergido(phi, phi_next, tolerancia=1e-5):
    not_zero = (phi_next != 0)
    diff_relativa = (phi - phi_next)[not_zero] / phi_next[not_zero]
    max_diff = np.max(np.fabs(diff_relativa))
    if max_diff > tolerancia:
        return True
    else:
        return False


w = 1.2

phi = np.zeros((N_pasos_x, N_pasos_y))
phi_next = np.zeros((N_pasos_x, N_pasos_y))

# iteracion
una_iteracion(phi, phi_next, N_pasos_x, N_pasos_y, h, w=1.2)
counter = 1

while counter < 5 and no_ha_convergido(phi, phi_next, tolerancia=1e-5):
    phi = phi_next.copy()
    una_iteracion(phi, phi_next, N_pasos_x, N_pasos_y, h, w=1.2)
    counter += 1

print("counter = {}".format(counter))


phi_next_transpuesta = phi_next.transpose()

fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-1, 1, N_pasos_x)
y = np.linspace(-1, 1, N_pasos_y)

X, Y = np.meshgrid(x, y)

ax.plot_surface(X, Y, phi_next_transpuesta, rstride=1, cstride=1)
ax.set_xlabel('$\ x $', fontsize=15)
ax.set_ylabel('$\ y $', fontsize=15)
ax.set_zlabel('$\ Potencial$', fontsize=15)

fig.show()

fig2 = plt.figure(2)
fig2.clf()
ax2 = fig2.add_subplot(111)
ax2.imshow(np.arcsinh(phi_next_transpuesta),
           origin='bottom', interpolation='nearest')
ax.set_xlabel('$\ x $', fontsize=15)
ax.set_ylabel('$\ y $', fontsize=15)

fig2.show()

plt.draw()
