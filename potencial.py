from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def muestra_phi(phi):
    print(phi[::-1, :])


def ro (i,j,ly,lx,h):
    x= i*h - lx/2 #me paro en el centro
    y= j*h -ly/2
    dx= 2.5 # vamos al borde
    dy= 3.5
    a=1 #ancho del dibujito
    p= 1/15 # densidad por cuadradito
    tot=0
    if x >= -dx and x<= dx+a:
        if y >= -dy and y <= dy:
            tot= p
    if x >= a-dx and x<= dx:
        if y >= -dy and y <= -dy +a:
            tot= p
    if x >= a-dx and x<= dx:
        if y >= dy-a and y <= dy:
            tot= p
    return tot

def g(j):
    return 1.



def una_iteracion(phi, phi_next,nx,ny, h, w=1.):
    for j in range(1, 10): #antes linea
        for i in range(1, nx-1):
            phi_next[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_next[i-1, j] +
                                       phi[i, j+1] + phi_next[i, j-1] ))
    for j in range (10,12): #en linea
        for i in range(1,10):
            phi_next[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_next[i-1, j] +
                                       phi[i, j+1] + phi_next[i, j-1] ))
        for i in range(40,50):
            phi_next[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_next[i-1, j] +
                                       phi[i, j+1] + phi_next[i, j-1] ))

        for j in range(10,11):#bajo
            for i in range (10,40):
                phi_next[i, j] = ((1 - w) * phi[i, j] +
                                  w / 3 * (phi[i+1, j] + phi_next[i-1, j] +
                                           phi[i, j-1] -
                                           h**2 * ro(i, j, h)+ h*-g(j)))
        for j in range(11,12):#sobre
            for i in range (10,40):
                phi_next[i, j] = ((1 - w) * phi[i, j] +
                                  w / 3 * (phi[i+1, j] + phi_next[i-1, j] +
                                           phi[i, j-1] -
                                           h**2 * ro(i, j, h)+ h*g(j)))


        for j in range(12, 20):#sobre la linea
            for i in range (1, nx-1):
                phi_next[i, j] = ((1 - w) * phi[i, j] +
                                  w / 4 * (phi[i+1, j] + phi_next[i-1, j] +
                                           phi[i, j+1] + phi_next[i, j-1] ))


        for j in range(20, 55):#rectangulo letra
            for i in range (1,10):
                phi_next[i, j] = ((1 - w) * phi[i, j] +
                                  w / 4 * (phi[i+1, j] + phi_next[i-1, j] +
                                           phi[i, j+1] + phi_next[i, j-1] ))
            for i in range (10, 40):
                phi_next[i, j] = ((1 - w) * phi[i, j] +
                                  w / 4 * (phi[i+1, j] + phi_next[i-1, j] +
                                           phi[i, j+1] + phi_next[i, j-1] ))
            for i in range (10, 40):
                phi_next[i, j] = ((1 - w) * phi[i, j] +
                                  w / 4 * (phi[i+1, j] + phi_next[i-1, j] +
                                           phi[i, j+1] + phi_next[i, j-1] +
                                           h**2 * ro(i, j, h) ))

        for j in range (55, ny-1):#sobre rectangulo
            for i in range (1,nx-1):
                phi_next[i, j] = ((1 - w) * phi[i, j] +
                                  w / 4 * (phi[i+1, j] + phi_next[i-1, j] +
                                           phi[i, j+1] + phi_next[i, j-1] ))


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

lx = 10
ly = 15
h = 0.2
N_pasos = h*lx
w=1.5
nx=lx/h
ny=ly/h


phi = np.zeros((nx, ny))
phi_next = np.zeros((nx, ny))

# iteracion
una_iteracion(phi, phi_next, nx,ny, h, w)
counter = 1
mx=4500
while counter < mx and no_ha_convergido(phi, phi_next):
    phi = phi_next.copy()
    una_iteracion(phi, phi_next, nx,ny, h, w)
    counter += 1

print("counter = {}".format(counter))
print(phi[(N_pasos - 1) / 2, (N_pasos - 1) / 2])

fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-1, 1, nx)
y = np.linspace(-1, 1, ny)

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
