
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


#Punto (0,0) en la esquina inferior izquierda de la grilla
def muestra_V(V):
    print(V[::-1,:])

def rho(i, j, h):
    x = i * h - 5
    y = j * h - 7.5
    rho_letra = 1 / 15
    rho_blanco = 0

    if y>=2.5 and y<=3.5 and x>=-2.5 and x<=2.5:
        return rho_letra
    if y<=-2.5 and y>=-3.5 and x>=-2.5 and x<=2.5:
        return rho_letra
    if y>=-2.5 and y<=2.5 and x>=-2.5 and x<=-1.5:
        return rho_letra
    else:
        return rho_blanco

def una_iteracion(V, V_next, N_pasosx, N_pasosy, h, w=1.):
    #Una iteracion
    #Iteracion Caja completa
    for i in range(1, int(N_pasosx) - 1):
        #Debajo de la linea
        for j in range(1,12):
            V_next[i, j] = ((1 - w) * V[i, j] +
                              w / 4 * (V[i+1, j] + V_next[i-1, j] +
                                       V[i, j+1] + V_next[i, j-1] +
                                       h**2 * rho(i, j, h)))
        #Encima de la linea
        for j in range(14, int(N_pasosy) - 1):
            V_next[i, j] = ((1 - w) * V[i, j] +
                              w / 4 * (V[i+1, j] + V_next[i-1, j] +
                                       V[i, j+1] + V_next[i, j-1] +
                                       h**2 * rho(i, j, h)))
    for j in range(12,14):
        #A la izquierda de la linea
        for i in range(1,11):
            V_next[i, j] = ((1 - w) * V[i, j] +
                              w / 4 * (V[i+1, j] + V_next[i-1, j] +
                                       V[i, j+1] + V_next[i, j-1] +
                                       h**2 * rho(i, j, h)))
        #Derecha de la linea
        for i in range(41,int(N_pasosx)-1):
            V_next[i, j] = ((1 - w) * V[i, j] +
                              w / 4 * (V[i+1, j] + V_next[i-1, j] +
                                       V[i, j+1] + V_next[i, j-1] +
                                       h**2 * rho(i, j, h)))

    #Iteracion condicion derivativa
    for i in range(11,41):
        #Puntos debajo de la linea: -1
        for j in range(12,13):
            V_next[i,j] = ((1 - w) * V[i, j] +
                              w / 3 * (V[i+1, j] + V_next[i-1, j] +
                                       V_next[i, j-1] + h**2 * rho(i, j, h) + h*(-1.)))
        #Puntos sobre la linea: +1
        for j in range(13,14):
            V_next[i,j] = ((1 - w) * V[i, j] +
                              w / 3 * (V[i+1, j] + V_next[i-1, j] +
                                       V_next[i, j-1] + h**2 * rho(i, j, h) + h*(1.)))

def no_ha_convergido(V, V_next, tolerancia=1e-2):
    not_zero = (V_next != 0)
    diff_relativa = (V - V_next)[not_zero] / V_next[not_zero]
    max_diff = np.max(np.fabs(diff_relativa))
    if max_diff > tolerancia:
        return True
    else:
        return False




#Main

#Setup
Lx = 10
Ly = 15
h= 0.2
N_pasosx = (Lx / h) + 1
N_pasosy = (Ly / h) + 1


V = np.zeros((N_pasosx, N_pasosy))
V_next= np.zeros((N_pasosx, N_pasosy))


#Iteracion
una_iteracion(V, V_next, N_pasosx, N_pasosy, h, w=1.)
counter = 1
while counter < 100 and no_ha_convergido(V, V_next, tolerancia=1e-2):
    V = V_next.copy()
    una_iteracion(V, V_next, N_pasosx, N_pasosy, h, w=1.)
    counter += 1

print("counter = {}".format(counter))


V_next_traspuesta=V_next.transpose()


fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-1, 1, N_pasosx)
y = np.linspace(-1, 1, N_pasosy)

X, Y = np.meshgrid(x, y)

ax.plot_surface(X, Y, V_next_traspuesta, rstride=1, cstride=1)
fig.show()

fig2 = plt.figure(2)
fig2.clf()
ax2 = fig2.add_subplot(111)
ax2.imshow(V_next_traspuesta, origin='bottom', interpolation='nearest')
fig2.show()

plt.draw()
