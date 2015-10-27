'''
Este script...
'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def muestra_v(v):
    print(v[::-1, :])


def rho(i, j, h):
    x = i * h - 5
    y = j * h - 7.5
    if y >= 2.5 and y <= 3.5 and x >= - 2.5 and x <= 2.5:
        return 1. / 15
    if y >= 1 and y <= 2.5 and x >= - 2.5 and x <= - 1.5:
        return 1. / 15
    if y >= 0 and y <= 1 and x >= - 2.5 and x <= 2.5:
        return 1. / 15
    if y >= - 3.5 and y <= 0 and x >= - 2.5 and x <= - 1.5:
        return 1. / 15
    else:
        return 0


# Se debe separar la iteracion en distintos segmentos:
# hay una ec para los puntos lejanos a la linea neumann
# hay otra para los inmediatamente vecinos a la linea neumann

def una_iteracion(v, v_next, N_pasos_x, N_pasos_y, h=0.2, w=1.2):
    for i in range(1, N_pasos_x-1):
        # abajo
        for j in range(1, 12):
            v_next[i, j] = ((1 - w) * v[i, j] +
                            w / 4 * (v[i+1, j] + v_next[i-1, j] +
                            v[i, j+1] + v_next[i, j-1] +
                            h**2 * rho(i, j, h)))
        # arriba
        for j in range(14, N_pasos_y-1):
            v_next[i, j] = ((1 - w) * v[i, j] +
                            w / 4 * (v[i+1, j] + v_next[i-1, j] +
                            v[i, j+1] + v_next[i, j-1] +
                            h**2 * rho(i, j, h)))

    for j in range(11, 15):
        # izq
        for i in range(1, 10):
            v_next[i, j] = ((1 - w) * v[i, j] +
                            w / 4 * (v[i+1, j] + v_next[i-1, j] +
                            v[i, j+1] + v_next[i, j-1] +
                            h**2 * rho(i, j, h)))
        # der
        for i in range(41, N_pasos_x-1):
            v_next[i, j] = ((1 - w) * v[i, j] +
                            w / 4 * (v[i+1, j] + v_next[i-1, j] +
                            v[i, j+1] + v_next[i, j-1] +
                            h**2 * rho(i, j, h)))

    # vecinos inmdiatos
    for i in range(10, 41):
        for j in range(12, 13):  # abajo
            v_next[i, j] = ((1 - w) * v[i, j] +
                            w / 3 * (v[i+1, j] + v_next[i-1, j] +
                            v_next[i, j-1] + h**2 * rho(i, j, h) + h*(-1.)))
        for j in range(13, 14):  # arriba
            v_next[i, j] = ((1 - w) * v[i, j] +
                            w / 3 * (v[i+1, j] + v_next[i-1, j] +
                            v_next[i, j-1] + h**2 * rho(i, j, h) + h*(1.)))


def no_ha_convergido(v, v_next, tolerancia=1e-3):
    not_zero = (v_next != 0)
    diff_relativa = (v - v_next)[not_zero] / v_next[not_zero]
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

N_pasos_x = int(Lx / h + 1)
N_pasos_y = int(Ly / h + 1)

v = np.zeros((N_pasos_x, N_pasos_y))
v_next = np.zeros((N_pasos_x, N_pasos_y))

una_iteracion(v, v_next, N_pasos_x, N_pasos_y, h, w=0.8)
counter = 1

while counter < 5000 and no_ha_convergido(v, v_next, tolerancia=1e-3):
    v = v_next.copy()
    una_iteracion(v, v_next, N_pasos_x, N_pasos_y, h, w=0.8)
    counter += 1

print("counter = {}".format(counter))

# trasponemos la matrix v_next
v_next_rotada = v_next.transpose()

# graficamos
fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-1, 1, N_pasos_x)
y = np.linspace(-1, 1, N_pasos_y)
X, Y = np.meshgrid(x, y)
ax.plot_surface(X, Y, v_next_rotada, rstride=1, cstride=1)
fig.show()
plt.savefig('plot_surface_08.png')

fig2 = plt.figure(2)
fig2.clf()
ax2 = fig2.add_subplot(111)
ax2.imshow(v_next_rotada, origin='bottom', interpolation='nearest')
fig2.show()
plt.savefig('plot_imshow_08.png')
