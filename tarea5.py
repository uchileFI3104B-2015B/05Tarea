from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def muestra_V(V):
    print(V[::-1, :])


def densidad_letra(i, j, h):
    '''Se busca donde esta la letra "L", asignandole el valor de su densidad'''
    x = i*h - 5
    y = j*h - 7.5
    letra = 1/11

    if y <= -2.5 and y >= -3.5 and x >= -3. and x <= 3.:
        return letra
    if y >= -2.5 and y <= 5.5 and x >= -3. and x <= -2.:
        return letra
    else:
        return 0


def una_iteracion(V, Vnext, Nx_pasos, Ny_pasos, h, w=1.):
    for i in range(1, int(Nx_pasos) - 1):
        for j in range(1, 13):  #Bajo linea
            Vnext[i, j] = ((1 - w)*V[i, j] + w/4*(V[i + 1, j] +
                            Vnext[i - 1, j] + V[i, j + 1] + Vnext[i, j - 1] +
                                 h**2*densidad_letra(i, j, h)))
        for j in range(15, int(Ny_pasos) - 1):  #Sobre linea
            Vnext[i, j] = ((1 - w)*V[i, j] + w/4*(V[i + 1, j] +
                            Vnext[i - 1, j] + V[i, j + 1] + Vnext[i, j - 1] +
                                 h**2*densidad_letra(i, j, h)))
    for j in range(13, 15):
        for i in range(1, 12):  #Izq. linea
            Vnext[i, j] = ((1 - w)*V[i, j] + w/4*(V[i + 1, j] +
                            Vnext[i - 1, j] + V[i, j + 1] + Vnext[i, j - 1] +
                                     h**2*densidad_letra(i, j, h)))
        for i in range(42, int(Nx_pasos) - 1):  #Der. linea
            Vnext[i, j] = ((1 - w)*V[i, j] + (w/4)*(V[i + 1, j] +
                            Vnext[i - 1, j] + V[i, j + 1] + Vnext[i, j - 1] +
                                     h**2*densidad_letra(i, j, h)))

    for i in range(12, 42):  #condicion derivada
        for j in range(13, 14):  #puntos debajo linea
            Vnext[i, j] = ((1 - w)*V[i, j] + w/3*(V[i + 1, j] +
                            Vnext[i - 1, j] + Vnext[i, j - 1] +
                                     h**2*densidad_letra(i, j, h) + h*(-1.)))
        for j in range(14, 15):  #puntos sobre linea
            Vnext[i, j] = ((1 - w)*V[i, j] + w/3*(V[i + 1, j] +
                            Vnext[i - 1, j] + Vnext[i, j - 1] +
                                     h**2*densidad_letra(i, j, h) + h*1.))


def no_ha_convergido(V, Vnext, tolerancia=1e-3):
    not_zero = (Vnext != 0)
    diff_relativa = (V - Vnext)[not_zero] / Vnext[not_zero]
    max_diff = np.max(np.fabs(diff_relativa))
    if max_diff > tolerancia:
        return True
    else:
        return False


# - - - Iteracion - - - #

Lx = 10
Ly = 15
h = 0.2
Nx_pasos = int(Lx/h)
Ny_pasos = int(Ly/h)

w = 0.001

V = np.zeros((Nx_pasos, Ny_pasos))
Vnext = np.zeros((Nx_pasos, Ny_pasos))

una_iteracion(V, Vnext, Nx_pasos, Ny_pasos, h, w)
counter = 1

while counter < 2000 and no_ha_convergido(V, Vnext, tolerancia=1e-4):
    V = Vnext.copy()
    una_iteracion(V, Vnext, Nx_pasos, Ny_pasos, h, w)
    counter += 1

print("counter = {}".format(counter))

Vnext_trans = Vnext.transpose()

x = np.linspace(-1, 1, Nx_pasos)
y = np.linspace(-1, 1, Ny_pasos)
X, Y = np.meshgrid(x, y)

fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Vnext_trans, rstride=1, cstride=1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Potencial')
fig.savefig("grafico3d.png")

fig2 = plt.figure(2)
fig2.clf()
ax2 = fig2.add_subplot(111)
ax2.imshow(np.arcsinh(Vnext_trans), origin='bottom', interpolation='nearest')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
fig2.savefig("grafico2d.png")
