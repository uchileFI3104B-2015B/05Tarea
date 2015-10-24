#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from caja import Caja

C = Caja()
C.agregar_letra_B()
A = C.get_carga()

plt.figure(1)
plt.imshow(A, origin='bottom', interpolation='nearest')
plt.colorbar()
plt.show()
plt.draw()
