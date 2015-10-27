#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Este script permite estudiar la relajación del rectángulo definido en caja.py,
sin la condición de borde derivativa sobre la línea.
'''

import numpy as np
import matplotlib.pyplot as plt
from caja import Caja

# Crear caja y calcular resultados
C = Caja()
C.agregar_letra_B()
for i in range(200):
    C.pasada_sobre_relajacion(1, "all")
V = C.get_potencial()
V_y = np.zeros(C.Ny)
for k in range(C.Ny):
    V_y[k] = V[k][20]

# Gráficos
y = C.reticulado * np.array(range(C.Ny))
fig = plt.figure(1)
plt.clf()
ax = fig.add_subplot(111)
ax.plot(y, V_y)
ax.set_xlabel('y [cm]')
ax.set_ylabel('V [C]')
ax.set_title('Perfil lateral del potencial')
plt.savefig('perfilletra.eps')

fig2 = plt.figure(2)
plt.clf()
plt.imshow(V, origin='bottom', interpolation='nearest',
           extent=[-5, 5, -7.5, 7.5])
plt.colorbar()
plt.title('Potencial electrostatico V [C]')
plt.xlabel('x [cm]')
plt.ylabel('y [cm]')
plt.savefig('Vletra.eps')
