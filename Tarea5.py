#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# Datos del cuadrilátero
Lx = 10
Ly = 15
h = 0.2
N_pasos_x = int(Lx / h)
N_pasos_y = int(Ly / h)


def RHO(i, j, h):
    '''
    Función que describe la distribución de la densidad
    de carga sobre la letra "A" del cuadrilatero.
    '''

    x = Lx / 2. - i * h    # Centrar x
    y = Ly / 2. - j * h    # Centrar y
    r = 1 / 20.            # Carga total / número de recuadros

    if (x >= -2.5 and x <= 2.5) and (y >= -3.5 and y <= 3.5):
        # Con esto estamos dentro del cuadriletaero de 5x7

        if (x >= -2.5 and x <= -1.5) or (x >= 1.5 and x <= 2.5):
            # Extremos izquierdo y derecho de A
            return r

        elif (y <= -2.5) and (x >= -1.5 and x <= 1.5):
            # Extremo superior de A
            return r

        elif (y >= -0.5 and y <= 1.5) and (x >= -1.5 and x <= 1.5):
            # Barra del centro de A
            return r
        else:
            # Todo lo que no pertenece a A
            return 0

    else:
        # Fuera del cuadrilatero
        return 0


def una_iteracion(V, V_next, N_pasos_x, N_pasos_y, h, w):
    '''
    Con esta funcionón lo que se busca es seccionar el cuadrilatero
    y calcular el potencial electrostático por zonas.
    '''

    for i in range(1, N_pasos_x - 1):

        for j in range(1, 10):
            # Debajo de la línea
            V_next[i, j] = ((1 - w) * V[i, j] + w / 4 *
                            (V[i+1, j] + V_next[i-1, j] +
                             V[i, j+1] + V_next[i, j-1] +
                             h**2 * RHO(i, j, h)))

        for j in range(12, N_pasos_y-1):
            # Por sobre la línea
            V_next[i, j] = ((1 - w) * V[i, j] + w / 4 *
                            (V[i+1, j] + V_next[i-1, j] +
                             V[i, j+1] + V_next[i, j-1] +
                             h**2 * RHO(i, j, h)))

    for j in range(10, 12):

        for i in range(1, 11):
            # A la izquierda de la línea
            V_next[i, j] = ((1 - w) * V[i, j] + w / 4 *
                            (V[i+1, j] + V_next[i-1, j] +
                             V[i, j+1] + V_next[i, j-1] +
                             h**2 * RHO(i, j, h)))

        for i in range(41, N_pasos_x-1):
            # A la derecha de la línea
            V_next[i, j] = ((1 - w) * V[i, j] + w / 4 *
                            (V[i+1, j] + V_next[i-1, j] +
                             V[i, j+1] + V_next[i, j-1] +
                             h**2 * RHO(i, j, h)))

    for i in range(10, 41):

        for j in range(10, 11):
            # Justo debajo de la línea
            V_next[i, j] = ((1 - w) * V[i, j] + w / 3 *
                            (V[i+1, j] + V_next[i-1, j] +
                             V_next[i, j-1] +
                             h**2 * RHO(i, j, h) - h))

        for j in range(11, 12):
            # Justo arriba de la línea
            V_next[i, j] = ((1 - w) * V[i, j] + w / 3 *
                            (V[i+1, j] + V_next[i-1, j] +
                             V_next[i, j-1] +
                             h**2 * RHO(i, j, h) + h))


def no_ha_convergido(V, V_next, tolerancia):
    '''
    Función que permite discernir si se ha convergido o no,
    con cierto rango de tolerancia.
    '''
    not_zero = (V_next != 0)
    diff_relativa = (V - V_next)[not_zero] / V_next[not_zero]
    max_diff = np.max(np.fabs(diff_relativa))
    if max_diff > tolerancia:
        return True
    else:
        return False

# Setup

V = np.zeros((N_pasos_x, N_pasos_y))
V_next = np.zeros((N_pasos_x, N_pasos_y))
w = 1.2

una_iteracion(V, V_next, N_pasos_x, N_pasos_y, h, w)

counter = 1
while counter < 2000 and no_ha_convergido(V, V_next, tolerancia=1e-2):
    V = V_next.copy()
    una_iteracion(V, V_next, N_pasos_x, N_pasos_y, h, w)
    counter += 1

print("counter = {}".format(counter))

V_next_traspuesta = V_next.transpose()  # Se graficaba no verticalmente

plt.figure(1)
plt.clf()
plt.imshow(V_next_traspuesta, origin='bottom',
           interpolation='nearest',
           extent=[-5, 5, -7.5, 7.5])
plt.colorbar()
plt.xlabel('x [cm]')
plt.ylabel('y [cm]')
plt.title('Potencial electrost'u'á''tico [V]')
plt.savefig('colores.png')
plt.show()

fig = plt.figure(2)
fig.clf()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-1, 1, N_pasos_x)
y = np.linspace(-1, 1, N_pasos_y)
X, Y = np.meshgrid(x, y)
ax.plot_surface(X, Y, V_next_traspuesta, rstride=1, cstride=1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Potencial electrost'u'á''tico [V] ')
fig.show()
plt.savefig('3d.png')
plt.title('Potencial electrost'u'á''tico [V] ')
fig.show()
plt.savefig('3d.png')
