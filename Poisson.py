#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
En este script se busca la manera de integrar un area con diferencias de
densidad electrica para obtener el valor del voltaje mediante el metodo de
sobrerelajacion
'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def muestra_phi(phi):
    '''
    Ejes modificados
    '''
    print(phi[::-1, :])
    pass


def Rho_Letra(i, j, h):
    '''
    Pide coordenadas de i y j (posicion) y le asigna el valor de la densidad
    proporcianado por la ecuacion de poisson y Laplace en el cuadrado de la
    letra
    '''
    # primero centramos las coordenadas
    x = i * h - 5
    y = j * h - 7.5
    value_rho = 1./15
    if y > -3.5 and y < 3.5 and x > -2.5 and x < -1.5:
        return value_rho
    if y > -3.5 and y < 3.5 and x >= 1.5 and x < 2.5:
        return value_rho
    if y > 0.5 and y < 2.5 and x > -1.5 and x < -0.5:
        return value_rho
    if y > 0.5 and y < 2.5 and x > 0.5 and x < 1.5:
            return value_rho
    if y > -0.5 and y < 1.5 and x > -0.5 and x < 0.5:
        return value_rho
    else:
        return 0


def una_iteracion(phi, phi_next, Nx_pasos, Ny_pasos, h, w=1.):
    '''
    Divide la superficie 10 sub areas las cuales cumplen distintas condiciones
    de densidad o de condicion derivativa. Se agrega condicion derivativa
    solo en las cercanias de la linea. Despues le asigna un valor analizando
    cada una de estas areas y entrega la grilla actualizada.
    '''
    # Parte Izquierda del area, la cual no contiene la letra
    for j in range(20, Ny_pasos - 1):
        for i in range(1, 13):
            phi_next[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_next[i-1, j] +
                                       phi[i, j+1] + phi_next[i, j-1]))

        # Parte Derecha del area, tampoco tiene letra
        for i in range(37, Nx_pasos - 1):
            phi_next[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_next[i-1, j] +
                                       phi[i, j+1] + phi_next[i, j-1]))

    # Parte Central Superior sobre la letra
    for i in range(13, 38):
        for j in range(55, Ny_pasos - 1):
            phi_next[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_next[i-1, j] +
                                       phi[i, j+1] + phi_next[i, j-1]))

        # Letra
        for j in range(20, 56):
            phi_next[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_next[i-1, j] +
                                       phi[i, j+1] + phi_next[i, j-1] +
                                       (h**2) * Rho_Letra(i, j, h)))
    # laterales de la linea
    for j in range(1, 20):
        # Parte izquierda de la linea
        for i in range(1, 11):
            phi_next[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_next[i-1, j] +
                                       phi[i, j+1] + phi_next[i, j-1]))

        # Parte derecha de la linea
        for i in range(40, Nx_pasos - 1):
            phi_next[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_next[i-1, j] +
                                       phi[i, j+1] + phi_next[i, j-1]))

    for i in range(11, 40):
        # Parte Central lejana bajo la linea
        for j in range(1, 10):
            phi_next[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_next[i-1, j] +
                                       phi[i, j+1] + phi_next[i, j-1]))

        # Parte Central Lejana sobre la linea
        for j in range(12, 20):
            phi_next[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_next[i-1, j] +
                                       phi[i, j+1] + phi_next[i, j-1]))

# Podria ponerse de inmediato j==12 sin embargo de esta forma es mas generico
    for i in range(11, 41):
        # inmediatamente bajo la linea
        for j in range(10, 11):
            y = 2 / h - 1
            phi_next[i, y] = ((1 - w) * phi[i, y] +
                              w / 3 * (phi[i+1, y] + phi_next[i-1, y] +
                                       phi_next[i, y-1] + h*(-1.)))

        # inmediatamente sobre la linea
        for j in range(11, 12):
            y = 2 / h + 1
            phi_next[i, y] = ((1 - w) * phi[i, y] +
                              w / 3 * (phi[i+1, y] + phi_next[i-1, y] +
                                       phi_next[i, y-1] + h*(1.)))


def no_ha_convergido(phi, phi_next, tolerancia=1e-5):
    not_zero = (phi_next != 0)
    diff_relativa = (phi - phi_next)[not_zero] / phi_next[not_zero]
    max_diff = np.max(np.fabs(diff_relativa))
    if max_diff > tolerancia:
        return True
    else:
        return False

# Main

# Setup

Lx = 10
Ly = 15
h = 0.2
Nx_pasos = int(Lx/h + 1)
Ny_pasos = int(Ly/h + 1)

v_rho = np.zeros((Nx_pasos, Ny_pasos))
v_rho_next = np.zeros((Nx_pasos, Ny_pasos))


# iteracion
una_iteracion(v_rho, v_rho_next, Nx_pasos, Ny_pasos, h, w=1.8)
counter = 1
while counter < 2000 and no_ha_convergido(v_rho, v_rho_next, tolerancia=1e-7):
    v_rho = v_rho_next.copy()
    una_iteracion(v_rho, v_rho_next, Nx_pasos, Ny_pasos, h, w=1.8)
    counter += 1

print("counter = {}".format(counter))

v_next_rotada = v_rho_next.transpose()


fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-5, 5, Nx_pasos)
y = np.linspace(-7.5, 7.5, Ny_pasos)
X, Y = np.meshgrid(x, y)
ax.plot_surface(X, Y, v_next_rotada, rstride=1, cstride=1)
fig.show()
plt.savefig('plot_surface.png')

fig2 = plt.figure(2)
fig2.clf()
plt.imshow(np.arcsinh(v_next_rotada), origin='bottom', interpolation='nearest',
           extent=[-5, 5, -7.5, 7.5])
plt.colorbar()
plt.title('Densidad de carga en el rect'u'á''ngulo')
plt.xlabel('x [cm]')
plt.ylabel('y [cm]')
fig2.show()

plt.savefig('plot_imshow.png')
