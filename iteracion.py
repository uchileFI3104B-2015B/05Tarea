#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from caja import Caja

C = Caja()
C.agregar_letra_B()
C.agregar_linea_horizontal()
A = C.get_carga()
V = C.get_potencial()

plt.clf()

plt.figure(1)
plt.imshow(A, origin='bottom', interpolation='nearest')
plt.colorbar()
plt.show()
plt.draw()

plt.clf()

plt.figure(2)
plt.imshow(V, origin='bottom', interpolation='nearest')
plt.colorbar()
plt.show()
plt.draw()

C.relaja(1,100)

V2 = C.get_potencial()

plt.clf()

plt.figure(3)
plt.imshow(V2, origin='bottom', interpolation='nearest')
plt.colorbar()
plt.show()
plt.draw()
