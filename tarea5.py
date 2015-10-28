#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Esta tarea resuelv la ecuacion de Poisson en 2D para el porencial electrostático
en una caja, con una letra M en el medio, y una línea con condiciones
derivativas
'''
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


Lx = 10
Ly = 15
h = 0.2
N_pasos_x = int(Lx / h)
N_pasos_y = int(Ly / h)


def RHO(i, j, h):
    ''' Retorna Rho para cuando está dentro de los cuadros que definfen M'''
    x = Lx / 2. - i * h    # La resta es para dejar el eje al centro
    y = Ly / 2. - j * h
    densidad = 0.5 / 20.
    if (x >= -2.5 and x <= 2.5) and (y >= -3.5 and y <= 3.5):
        # Esta condicion es para entrar a la caja donde esta M
        if (x >= -2.5 and x <= -1.5) or (x >= 1.5 and x <= 2.5):
            # Lineas a los lados de M
            return densidad

        elif (x >= -1.5 and x <= -0.5) and (y >= 0.5 and y >= 2.5):
            # Barrita a la izquierda
            return densidad

        elif (x >= 0.5 and x <= 1.5) and (y >= 0.5 and y <= 2.5):
            # Barrita a la derecha
            return densidad

        elif (x >= -0.5 and x <= 0.5) and (y >= -0.5 and y <= 1.5):
            # Barrita al medio
            return densidad

        else:
            # Dentro del area de la letra pero no es la letra M
            return 0

    else:
        # Fuera del area de la letra
        return 0


def una_iteracion(V, V_next, N_pasos_x, N_pasos_y, h, w):
    '''
    Realiza una iteracion, la cual se divide en varias partes dependiendo
    de en qué lado de la caja se esté
    '''
    for i in range(1, N_pasos_x - 1):
        # Seccion arriba de la letra
        for j in range(1, 20):
            V_next[i, j] = ((1 - w) * V[i, j] +
                            (w / 4.) * (V[i + 1, j] + V_next[i - 1, j] +
                                        V[i, j + 1] + V_next[i, j - 1]))

    for j in range(20, 56):
        for i in range(1, 13):            # Lateral izquierdo letra
            V_next[i, j] = ((1 - w) * V[i, j] +
                            (w / 4.) * (V[i + 1, j] + V_next[i - 1, j] +
                                        V[i, j + 1] + V_next[i, j - 1]))
        for i in range(37, N_pasos_x - 1):        # Lateral derecho letra
            V_next[i, j] = ((1 - w) * V[i, j] +
                            (w / 4.) * (V[i + 1, j] + V_next[i - 1, j] +
                                        V[i, j + 1] + V_next[i, j - 1]))
        for i in range(13, 37):             # Letra
            V_next[i, j] = ((1 - w) * V[i, j] +
                            (w / 4.) * (V[i + 1, j] + V_next[i - 1, j] +
                                        V[i, j + 1] + V_next[i, j - 1] +
                                        (h**2) * RHO(i, j, h)))

    for j in range(56, N_pasos_y - 1):
        for i in range(1, 10):
            V_next[i, j] = ((1 - w) * V[i, j] +
                            (w / 4.) * (V[i + 1, j] + V_next[i - 1, j] +
                                        V[i, j + 1] + V_next[i, j - 1]))

        for i in range(40, N_pasos_x - 1):
            V_next[i, j] = ((1 - w) * V[i, j] +
                            (w / 4.) * (V[i + 1, j] + V_next[i - 1, j] +
                                        V[i, j + 1] + V_next[i, j - 1]))

    for i in range(10, 40):

        for j in range(56, N_pasos_y - 1):
            if (j == 13 / h - 1):
                # esta sobre la Linea
                y = 13. / h - 1
                V_next[i, y] = ((1 - w) * V[i, y] +
                                w / 3 * (V_next[i - 1, y] + V[i + 1, y] +
                                         V_next[i, y + 1] - h * 1))
            elif (j == 13 / h + 1):
                # esta bajo la linea
                y = 13. / h + 1
                V_next[i, y] = ((1 - w) * V[i, y] +
                                w / 3 * (V_next[i - 1, y] + V[i + 1, y] +
                                         V_next[i, y - 1] + h*1))
            else:
                V_next[i, j] = ((1 - w) * V[i, j] +
                                (w / 4.) * (V[i + 1, j] + V_next[i - 1, j] +
                                            V[i, j + 1] + V_next[i, j - 1]))


def no_ha_convergido(V, V_next, tolerancia):
    '''
    Retorna True si no cumple una cierta tolerancia,
    y False si es que la cumple
    '''
    not_zero = (V_next != 0)
    diff_relativa = (V - V_next)[not_zero] / V_next[not_zero]
    max_diff = np.max(np.fabs(diff_relativa))
    if max_diff > tolerancia:
        return True
    else:
        return False

# Main

# Setup

V = np.zeros((N_pasos_x, N_pasos_y))
V_next = np.zeros((N_pasos_x, N_pasos_y))
w = 1.4

# Matriz que define rho
rho = np.zeros((Lx / h, Ly / h))


una_iteracion(V, V_next, N_pasos_x, N_pasos_y, h, w)
counter = 1
while counter < 3000 and no_ha_convergido(V, V_next, tolerancia=1e-2):
    V = V_next.copy()
    una_iteracion(V, V_next, N_pasos_x, N_pasos_y, h, w)
    counter += 1

print("counter = {}".format(counter))

V_next_rotada = V_next.transpose()

fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-1, 1, N_pasos_x)
y = np.linspace(-1, 1, N_pasos_y)
X, Y = np.meshgrid(x, y)
ax.plot_surface(X, Y, V_next_rotada, rstride=1, cstride=1)
plt.xlabel('x [cm]')
plt.ylabel('y [cm]')
plt.title('Potencial electrost'u'á''tico ')
fig.show()
#plt.savefig('plot_surface.png')

plt.figure(2)
plt.clf()
plt.imshow(V_next_rotada, origin='bottom', interpolation='nearest')
plt.colorbar()
plt.xlabel('x [cm]')
plt.ylabel('y [cm]')
plt.title('Potencial electrost'u'á''tico ')
#plt.savefig('plot_imshow.png')
plt.show()
