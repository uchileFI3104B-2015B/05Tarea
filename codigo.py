from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def muestra_phi(phi):
    print(phi[::-1, :])


def q(espacio, i, j, h):
    paso=h

    return espacio[i,j]




def una_iteracion(phi, phi_next, espacio, N_pasosX, N_pasosY, h, w=1.):
'''
dividimos los casos segun su posicion respecto la linea de condicion de borde, esta se encuentra entre las coordenadas
y=[8,13 y x=[11,41] , estas son coordenadas dentro de la matriz "espacio"
'''

    for i in range(1,N_pasosX-1):
        for j in range(0,7): #abajo de la línea
            phi_next[i,j]=((1-w)*phi[i,j]+(w/4.)*(phi[i+1,j]+phi_next[i-1,j]+phi[i,j+1]+phi_next[i,j-1]+h**2*q(espacio,i ,j ,h)))
        for j in range(14,N_pasosY-1): #arriba de la línea
            phi_next[i,j]=((1-w)*phi[i,j]+(w/4.)*(phi[i+1,j]+phi_next[i-1,j]+phi[i,j+1]+phi_next[i,j-1]+h**2*q(espacio,i ,j ,h)))
    for j in range(7,14):
        for i in range(0,9): #a la izquierda de la línea
            phi_next[i,j]=((1-w)*phi[i,j]+(w/4.)*(phi[i+1,j]+phi_next[i-1,j]+phi[i,j+1]+phi_next[i,j-1]+h**2*q(espacio,i ,j ,h)))
        for i in range(40,N_pasosX-1): #a la derecha de la línea
            phi_next[i,j]=((1-w)*phi[i,j]+(w/4.)*(phi[i+1,j]+phi_next[i-1,j]+phi[i,j+1]+phi_next[i,j-1]+h**2*q(espacio,i ,j ,h)))
    for i in range(11,41):
        for j in range(7,8): #justo debajo de la línea, donde aplica la condición -1
            phi_next[i,j]=((1-w)*phi[i,j]+(w/3.)*(phi[i+1,j]+phi_next[i-1,j]+phi_next[i,j-1]+h**2*q(espacio,i ,j ,h)-h))
        for j in range(13,14): #justo sobre la línea, donde aplica la condición +1
            phi_next[i,j]=((1-w)*phi[i,j]+(w/3.)*(phi[i+1,j]+phi_next[i-1,j]+phi_next[i,j-1]+h**2*q(espacio,i,j,h)+h))





def no_ha_convergido(phi, phi_next, tolerancia=1e-5):
    not_zero = (phi_next != 0)
    diff_relativa = (phi - phi_next)[not_zero] / phi_next[not_zero]
    max_diff = np.max(np.fabs(diff_relativa))
    if max_diff > tolerancia:
        return True
    else:
        return False







Lx = 10
Ly = 15
h = 0.2
a = int(1/h) #número de pasos en 1 cuadrado
N_pasosX = int((Lx/h) +1) #cantidad de elementos desde y=0 hasta y=15
N_pasosY = int((Ly/h) +1) #analogo
paso=h

espacio= np.zeros((N_pasosX, N_pasosY))  #primer indice es le eje X (filas) y el segundo el eje Y (columnas)


for i in range (13,13+a):
    for j in range (18, 55):
        espacio[i,j]=1/15.

#reyenamos para y=[-7,5;7,5] las coordenadas x
for j in range (50,55):
    for i in range(13, 38):
        espacio[i,j]=1/15.

#reyenamos para y=[7,8] las coordenadas x
for j in range (40,45):
    for i in range(13, 38):
        espacio[i,j]=1/15.


phi = np.zeros((N_pasosX, N_pasosY))
phi_next = np.zeros((N_pasosX, N_pasosY))

# iteracion
una_iteracion(phi, phi_next, espacio, N_pasosX, N_pasosY, h, 1)
counter = 1
while counter < 100 and no_ha_convergido(phi, phi_next, tolerancia=1e-7):
    phi = phi_next.copy()
    una_iteracion(phi, phi_next, espacio, N_pasosX, N_pasosY, h, w=0.8)
    counter += 1

print("counter = {}".format(counter))
#print(phi[(N_pasos - 1) / 2, (N_pasos - 1) / 2])


phi_trans=phi_next.transpose()

fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-1, 1, N_pasosX)
y = np.linspace(-1, 1, N_pasosY)

X, Y = np.meshgrid(x,y)

ax.plot_surface(X, Y, phi_trans, rstride=1, cstride=1)
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title("Reprecentacion tridimencional del potencial actuando sobre la superficie")
fig.show()

fig2 = plt.figure(2)
fig2.clf()
ax2 = fig2.add_subplot(111)
ax2.imshow(phi_trans, origin='bottom', interpolation='nearest')
ax2.contour(phi_trans, origin='lower')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title("Grafico del potencial actuando sobre la superficie")
fig2.show()

plt.draw()
