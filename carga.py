from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

'''
Grafica la carga del sistema
'''


def r(i, j, Lx, Ly, h):
    x = i * h - Lx / 2
    y = j * h - Ly / 2
    dx = 2.5
    dy = 3.5
    l = 1
    rho = 1 / 11.
    r = 0
    if x >= -dx and x <= -dx + l:
        if y >= -dy and y <= dy:
            r = rho
    elif x >= l - dx and x <= dx:
        if y >= -dy and y <= -dy + l:
            r = rho
    return r


Lx = 10
Ly = 15
h = 0.2
N_x = int(Lx / h)
N_y = int(Ly / h)
c = np.zeros((N_x, N_y))
for i in range(0, N_x - 1):
    for j in range(0, N_y - 1):
        c[i, j] = r(i, j, Lx, Ly, h)

c_tras = c.transpose()
fig2 = plt.figure(2)
fig2.clf()
ax2 = fig2.add_subplot(111)
ax2.imshow(c_tras, origin='bottom', interpolation='nearest')
ax2.contour(c_tras, origin='lower')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
plt.savefig('carga.png')
fig2.show()
