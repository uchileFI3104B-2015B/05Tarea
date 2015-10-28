#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


class circuito(object):

    def __init__(self, ancho, largo, paso):
        self.N_puntos_x = int(ancho / paso) + 1
        self.N_puntos_y = int(largo / paso) + 1
        self.x = np.linspace(- ancho / 2, ancho / 2, self.N_puntos_x)
        self.y = np.linspace(- largo / 2, largo / 2, self.N_puntos_y)
        self.v = np.zeros((self.N_puntos_y, self.N_puntos_x))
        self.dv = np.zeros((self.N_puntos_y, self.N_puntos_x))
        self.densidad_carga = np.zeros((self.N_puntos_y, self.N_puntos_x))

    def cargar_segmento(self, px, py, dx, dy, q, paso):
        '''
        carga un segmento lineal desde la posicion (px,py)
        con un ancho dx y un lago dy, por defecto se crea un cuadrado de area
        1[cm^2] todos los parametros se deben entregar en centimetros
        '''
        bloques_x = int(dx / paso)
        bloques_y = int(dy / paso)
        x_inicial = int((px + 5) / paso)
        y_inicial = int((px + 5) / paso)
        x_final = x_inicial + bloques_x
        y_final = y_inicial + bloques_y

        for i in range(x_inicial, x_final):
            for j in range(y_inicial, y_final):
                self.densidad_carga[j][i] = q

    def cargar_J(self, px, py, a, l, q, paso):
        '''
        carga los segmentos necesatios para formar la letra J en una
        caja de ancho "a" y largo "l"
        '''
        for i in range(25, 75):
            for j in range(100, 110):
                self.densidad_carga[j][i] = q

        for i in range(45, 55):
            for j in range(35, 110):
                self.densidad_carga[j][i] = q

        for i in range(25, 45):
            for j in range(35, 45):
                self.densidad_carga[j][i] = q

        for i in range(25, 35):
            for j in range(45, 55):
                self.densidad_carga[j][i] = q


# --------------------Ahora se calcula la solucion del sistema------------- #
def iteracion_sobrerelajacion_dirichlet(V, V_next, DV, N_pasos_x,
                                        N_pasos_y, h, rho, w=1.2):
    for j in range(1, N_pasos_x-1):
        for i in range(1, N_pasos_y-1):
            V_next[i, j] = ((1 - w) * V[i, j] +
                            w / 4 * (V[i+1, j] + V_next[i-1, j] +
                                     V[i, j+1] + V_next[i, j-1] +
                                     h**2 * rho[i, j]))


def iteracion_sobrerelajacion_newmman(V, V_next, DV, N_pasos_x,
                                      N_pasos_y, h, rho, w=1.2):

    for j in range(1, N_pasos_x-1):
        for i in range(1, N_pasos_y-1):
            if j > 20 and j < 80 and i == 20:

                # lineas antes de los bordes #
                V_next[19, j] = ((1 - w) * V[19, j] +
                                 w / 3 * (V[19, j+1] +
                                          V_next[19, j-1] +
                                          V[20, j] + V_next[18, j] +
                                          h**2 * rho[19, j] +
                                          h * (-1)))

                V_next[21, j] = ((1 - w) * V[21, j] +
                                 w / 3 * (V[21, j+1] + V_next[21, j-1] +
                                          V[20, j] + V_next[22, j] +
                                          h**2 * rho[21, j] +
                                          h * (1)))
            else:
                V_next[i, j] = ((1 - w) * V[i, j] +
                                w / 4 * (V[i+1, j] + V_next[i-1, j] +
                                         V[i, j+1] + V_next[i, j-1] +
                                         h**2 * rho[i, j]))

h = 0.1
rho = 1/27
c = circuito(10, 15, h)
c.cargar_J(2.5, 3.5, 5, 7, rho, h)
V_next = np.zeros((c.N_puntos_y, c.N_puntos_x))


# iteracion #
while counter < 200:
    c.v = V_next.copy()
    iteracion_sobrerelajacion_newmman(c.v, V_next, c.dv, c.N_puntos_x,
                                      c.N_puntos_y, h, c.densidad_carga,
                                      w=1.2)
    counter += 1

fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-1, 1, c.N_puntos_x)
y = np.linspace(-1, 1, c.N_puntos_y)

X, Y = np.meshgrid(x, y)

ax.plot_surface(X, Y, np.arcsinh(V_next), rstride=1, cstride=1)
fig.show()

fig2 = plt.figure(2)
fig2.clf()
ax2 = fig2.add_subplot(111)
ax2.imshow(np.arcsinh(V_next), origin='bottom', interpolation='nearest')
fig2.show()

plt.draw()
