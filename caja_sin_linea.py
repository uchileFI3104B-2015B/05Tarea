#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from caja import Caja

C = Caja()
C.agregar_letra_B()
#C.agregar_linea_horizontal(dV=0.1)
for i in range(1000):
    C.pasada_sobre_relajacion(1,"all")
C.relaja(1,1000)
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

plt.figure(2)
plt.imshow(V, origin='bottom', interpolation='nearest') #, vmin=-3, vmax=3)
plt.colorbar()
plt.show()
plt.draw()
