'''
Descripcion
'''
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# Definimos la funcion rho que asignara un valor de densidad
# a cada punto de la grilla, diferenciando los espacios en
# blanco de los espacios que pertenecen a la letra 'B'


def rho(i, j, h):
    x = i * h - 5
    y = j * h - 7.5
    rho_letra = 1 / 23
    rho_blanco = 0

    if x >= -2.5 and x <= -1.5 and y >= -3.5 and y <= 3.5:
        return rho_letra
    if x >= 1.5 and x <= 2.5 and y >= -3.5 and y <= 3.5:
        return rho_letra
    if y <= 3.5 and y >= 2.5 and x > -1.5 and x < 1.5:
        return rho_letra
    if y <= 0.5 and y >= -0.5 and x > -1.5 and x < 1.5:
        return rho_letra
    if y <= -2.5 and y >= -3.5 and x > -1.5 and x < 1.5:
        return rho_letra
    else:
        return rho_blanco

# Definimos la funcion 'una_iteracion'


def una_iteracion(V, V_next, N_pasos_x, N_pasos_y, h, w):
    for i in range(1, int(N_pasos_x) - 1):
        # Separamos la grilla para aislar el lugar con condicion derivativa

        # Bajo la condicion derivativa
        for j in range(1, 12):
            V_next[i, j] = ((1 - w) * V[i, j] +
                            w / 4 * (V[i+1, j] + V_next[i-1, j] +
                            V[i, j+1] + V_next[i, j-1] + h**2 * rho(i, j, h)))

        # sobre la condicion derivativa
        for j in range(14, int(N_pasos_y) - 1):
            V_next[i, j] = ((1 - w) * V[i, j] +
                            w / 4 * (V[i+1, j] + V_next[i-1, j] +
                            V[i, j+1] + V_next[i, j-1] + h**2 * rho(i, j, h)))

    for j in range(12, 14):
        # A la izquierda de la condicion derivativa
        for i in range(1, 11):
            V_next[i, j] = ((1 - w) * V[i, j] +
                            w / 4 * (V[i+1, j] + V_next[i-1, j] +
                            V[i, j+1] + V_next[i, j-1] + h**2 * rho(i, j, h)))

        # A la derecha de la condicion derivativa
        for i in range(41, int(N_pasos_x)-1):
            V_next[i, j] = ((1 - w) * V[i, j] +
                            w / 4 * (V[i+1, j] + V_next[i-1, j] +
                            V[i, j+1] + V_next[i, j-1] + h**2 * rho(i, j, h)))

    # Ahora iteramos dentro de la condicion derivativa
    for i in range(11, 41):
        # Bajo la condicion derivativa -1
        for j in range(12, 13):
            V_next[i, j] = ((1 - w) * V[i, j] +
                            w / 3 * (V[i+1, j] + V_next[i-1, j] +
                            V[i, j-1] + h**2 * rho(i, j, h) + h*(-1.)))

        # Sobre la condicion derivativa +1
        for j in range(13, 14):
            V_next[i, j] = ((1 - w) * V[i, j] +
                            w / 3 * (V[i+1, j] + V_next[i-1, j] +
                            V[i, j-1] + h**2 * rho(i, j, h) + h*(1.)))


def no_ha_convergido(V, V_next, tolerancia):
    not_zero = (V_next != 0)
    diff_relativa = (V - V_next)[not_zero] / V_next[not_zero]
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
N_pasos_x = Lx / h + 1
N_pasos_y = Ly / h + 1
w = 1
tolerancia = 1e-5
iteraciones = 10

# Creamos la grilla
V = np.zeros((N_pasos_x, N_pasos_y))
V_next = np.zeros((N_pasos_x, N_pasos_y))

# Probamos para 10 iteraciones
una_iteracion(V, V_next, N_pasos_x, N_pasos_y, h, w)
counter = 1
while counter < iteraciones and no_ha_convergido(V, V_next, tolerancia):
    V = V_next.copy()
    una_iteracion(V, V_next, N_pasos_x, N_pasos_y, h, w)
    counter += 1

print("counter = {}".format(counter))


# Graficamos

V_next_trans = V_next.transpose()

fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-1, 1, N_pasos_x)
y = np.linspace(-1, 1, N_pasos_y)

X, Y = np.meshgrid(x, y)

ax.plot_surface(X, Y, V_next_trans, rstride=1, cstride=1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('V Potencial')
fig.show()

fig2 = plt.figure(2)
fig2.clf()
ax2 = fig2.add_subplot(111)
ax2.imshow(V_next_trans, origin='bottom', interpolation='nearest')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
fig2.show()

plt.draw()
