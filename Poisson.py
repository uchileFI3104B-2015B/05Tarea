
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
    #print(phi[::-1, :])
    pass


def DensidadLetra(i, j, h):
    '''
    Pide coordenadas de i y j (posicion) y le asigna el valor de la densidad
    proporcianado por la ecuacion de poisson y Laplace en el cuadrado de la letra
    '''
    #primero centramos las coordenadas
    x = i * h - 5
    y = j * h - 7.5
    value = 1./15 #rho dividido en la superficie
    #Letra M
    if y>=-3.5 and y<=3.5 and x>=-2.5 and x<=-1.5:
        return value
    if y>=-3.5 and y<=3.5 and x>=1.5 and x<=2.5:
        return value
    if y>=0.5 and y<=2.5 and x>=-1.5 and x<=-0.5:
        return value
    if y>=0.5 and y<=2.5 and x>=0.5 and x<=1.5:
            return value
    if y>=-0.5 and y<=1.5 and x>=-0.5 and x<=0.5:
        return value
    else:
        return 0
'''
def una_iteracion(phi, phi_next, N_pasos, h, w=1.):
    for i in range(1, N_pasos-1):
        for j in range(1, N_pasos-1):
            phi_next[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_next[i-1, j] +
                                       phi[i, j+1] + phi_next[i, j-1] +
                                       h**2 * q(i, j, h)))


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

Lx = Ly = 2
N_pasos = 21
h = Lx / (N_pasos - 1)

phi = np.zeros((N_pasos, N_pasos))
phi_next = np.zeros((N_pasos, N_pasos))

# iteracion
una_iteracion(phi, phi_next, N_pasos, h, w=1.)
counter = 1
while counter < 800 and no_ha_convergido(phi, phi_next, tolerancia=1e-7):
    phi = phi_next.copy()
    una_iteracion(phi, phi_next, N_pasos, h, w=0.8)
    counter += 1

print("counter = {}".format(counter))
print(phi[(N_pasos - 1) / 2, (N_pasos - 1) / 2])

fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-1, 1, N_pasos)
y = np.linspace(-1, 1, N_pasos)

X, Y = np.meshgrid(x, y)

ax.plot_surface(X, Y, phi_next, rstride=1, cstride=1)
fig.show()

fig2 = plt.figure(2)
fig2.clf()
ax2 = fig2.add_subplot(111)
ax2.imshow(phi_next, origin='bottom', interpolation='nearest')
ax2.contour(phi_next, origin='lower')
fig2.show()

plt.draw()
'''
