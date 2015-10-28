"""
scrip que reslueve usando sobre_relajacion sucesiva (SOR) la ecuacion de
Poisson en una caja de 10[cm]x15[cm], con una letra J dentro con densidad de
 carga constante y carga total 1[C] También existe una condicion de borde
 derivativa en y = -5.5[cm]; x=[-3: 3][cm].
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def densidad(i, j, h):
    """
    Funcion que recibe coordenadas de un punto y entrega la densidad de carga
    en ese punto. (0 fuera de la letra y constante en la letra)
    """
    puntos_en_letra = 378.0
    if ((15 <= i <= 20) and (20 <= j <= 36) or
        (21 <= i <= 29) and (20 <= j <= 25) or
       (30 <= i <= 35) and (20 <= j <= 54)):
        densidad_en_punto = 1/puntos_en_letra

    else:
        densidad_en_punto = 0

    return densidad_en_punto


def una_iteracion(V, V_next, numero_celdas_x, numero_celdas_y, h, w=1,
                  condicion_derivativa=True):
    """
    funcion que realiza una iteracion sobre la caja con las formulas del metodo
    SOR dependiendo el punto donde se calcule el potencial (sobre la linea,
    bajo la linea, en la linea, o en otro lugar). Si condicion_derivativa es
    False, no considera la condicion derivativa en la iteracion.
    """
    if condicion_derivativa is True:
        for i in range(1, numero_celdas_x-1):
            for j in range(1, numero_celdas_y-1):
                if 10 <= i <= 40 and j == 11:
                    V_next[i, j] = ((1 - w) * V[i, j] +
                                    (w / 3.) * (V[i+1, j] +
                                    V_next[i-1, j] +
                                    V_next[i, j+1] -
                                    densidad(i, j, h)*h**2 - h*g))
                elif 10 <= i <= 40 and j == 9:
                    V_next[i, j] = ((1 - w) * V[i, j] +
                                    (w / 3.0) * (V[i+1, j] +
                                    V_next[i-1, j] +
                                    V_next[i, j-1] -
                                    densidad(i, j, h)*h**2 + h*g))
                elif 10 <= i <= 40 and j == 10:
                    V_next[i, j] = V_next[i, j-1] + h*g

                else:
                    V_next[i, j] = ((1 - w) * V[i, j] +
                                    (w / 4.) * (V[i+1, j] +
                                    V_next[i-1, j] + V[i, j+1] +
                                    V_next[i, j-1] - densidad(i, j, h)*h**2))
    else:
        for i in range(1, numero_celdas_x-1):
            for j in range(1, numero_celdas_y-1):
                V_next[i, j] = ((1 - w) * V[i, j] +
                                (w / 4.) * (V[i+1, j] +
                                V_next[i-1, j] + V[i, j+1] +
                                V_next[i, j-1] - densidad(i, j, h)*h**2))
    pass


def no_ha_convergido(V, V_next, tolerancia=1e-5):
    """
    funcion que retorna True si no se cumple la condicion de convergencia
    (diferencia relativa entre valores del potencial entre una iteracion y la
    siguiente menorque tolerancia elegida). Retorna False si se cumple.
    """
    not_zero = (V_next != 0)
    diff_relativa = (V - V_next)[not_zero] / V_next[not_zero]
    max_diff = np.max(np.fabs(diff_relativa))
    if max_diff > tolerancia:
        return True
    else:
        return False


# setup
h = 0.2
ancho = 10
alto = 15
numero_celdas_x = int(ancho/h + 1)
numero_celdas_y = int(alto/h + 1)
g = 1
V = np.zeros((numero_celdas_x, numero_celdas_y))
V_next = np.zeros((numero_celdas_x, numero_celdas_y))
V_sin_cond_derivativa = np.zeros((numero_celdas_x, numero_celdas_y))
V_sin_cond_derivativa_next = np.zeros((numero_celdas_x, numero_celdas_y))

# Main

# interaciones sin considerar condicion de borde derivativa

# primera iteracion
una_iteracion(V_sin_cond_derivativa, V_sin_cond_derivativa_next,
              numero_celdas_x, numero_celdas_y, h, w=1.8,
              condicion_derivativa=False)
counter = 1

while counter < 3000 and no_ha_convergido(V_sin_cond_derivativa,
                                          V_sin_cond_derivativa_next,
                                          tolerancia=1e-5):
    V_sin_cond_derivativa = V_sin_cond_derivativa_next.copy()
    una_iteracion(V_sin_cond_derivativa, V_sin_cond_derivativa_next,
                  numero_celdas_x, numero_celdas_y, h, w=1.8,
                  condicion_derivativa=False)
    counter += 1

# interaciones considerando condicion de borde derivativo

# primera iteracion

una_iteracion(V, V_next, numero_celdas_x, numero_celdas_y, h, w=1.8)
counter = 1

while counter < 3000 and no_ha_convergido(V, V_next, tolerancia=1e-4):
    V = V_next.copy()
    una_iteracion(V, V_next, numero_celdas_x, numero_celdas_y, h, w=1.8)
    counter += 1
print("counter = {}".format(counter))

# graficar soluciones
# sin incluir condicion derivativa


fig1 = plt.figure(1)
fig1.clf()
ax1 = fig1.add_subplot(111)
plt.imshow(V_sin_cond_derivativa_next.transpose(), origin='botton',
           interpolation='nearest')
ax1.set_xlabel("X [cm]")
ax1.set_ylabel("Y [cm]")
ax1.set_title("Potencial sin condicion derivativa [ergs/C]")
fig1.show()
# incluyendo condicion derivativa
fig2 = plt.figure(2)
fig2.clf()
ax2 = fig2.add_subplot(111, projection='3d')

x = np.linspace(-1, 1, numero_celdas_x)
y = np.linspace(-1, 1, numero_celdas_y)

X, Y = np.meshgrid(x, y)

ax2.plot_surface(X, Y, V_next.transpose(), rstride=1, cstride=1)
ax2.set_xlabel("X [cm]")
ax2.set_ylabel("Y [cm]")
ax2.set_zlabel("potecial [ergs/C]")
ax2.set_title("Potencial con condicion derivativa ")
fig2.show()

fig3 = plt.figure(3)
fig3.clf()
ax3 = fig3.add_subplot(111)
plt.imshow(V_next.transpose(), origin='botton', interpolation='nearest')
ax3.contour(V_next.transpose(), origin='lower')
ax3.set_xlabel("X [cm]")
ax3.set_ylabel("Y [cm]")
ax3.set_title("Potencial con condicion derivativa")
fig3.show()
