#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from caja import Caja

C = Caja()
C.agregar_letra_B()
for i in range(200):
    C.pasada_sobre_relajacion(1,"all")
V = C.get_potencial()
V_y = np.zeros(C.Ny)
for k in range(C.Ny):
    V_y[k] = V[k][20]

y = C.reticulado * np.array(range(C.Ny))
fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.plot(y,V_y)
plt.show()
plt.draw()

fig2 = plt.figure(2)
plt.clf()
plt.imshow(V, origin='bottom', interpolation='nearest', extent= [-5,5,-7.5,7.5])
plt.colorbar()
plt.title('Potencial electrostatico V [C]')
plt.savefig('Vletra.eps')
