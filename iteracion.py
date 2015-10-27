#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Este script permite graficar los resultados de relajar un rectángulo sujeto a
la ecuación de Poisson, definido en la clase Caja. También permite estudiar la
convergencia de las soluciones para distintos valores del parámetro w en el
método de sobre-relajación.
'''

import numpy as np
import matplotlib.pyplot as plt
from caja import Caja


def convergencia(C, arreglo_w):
    '''
    Esta función permite evaluar la convergencia del método de sobre-relajación
    sucesiva a la solución de la ecuación de Poisson. Recibe como parámetros
    un objeto de la clase Caja y un arreglo con los w a estudiar. Retorna el
    número de iteraciones que tomó converger y el potencial correspondiente a
    cada una de las soluciones.
    '''
    C.resetea_potencial()
    C.relaja(1, 1000)
    V_obj = C.get_potencial()
    N_w = []
    V_w = []
    for w in arreglo_w:
        print "w =", w
        C.resetea_potencial()
        chi2 = 50.0
        n = 0
        while chi2 > 15 and n < 10000:
            paso = int(np.ceil(chi2/100.0))
            C.relaja(w, paso)
            n += paso
            chi2 = np.sum(np.power(C.get_potencial() - V_obj, 2))
        if n >= 10000:
            N_w.append(10001)
            print "No converge después de 10000 iteraciones"
        else:
            N_w.append(n)
            print "Converge después de", n, "iteraciones"
        V_w.append(C.get_potencial())
        print ""
    return N_w, V_w

# Crear Caja y calcular resultados
C = Caja()
C.agregar_letra_B()
C.agregar_linea_horizontal()
rango_w = np.linspace(0.2, 1.8, 9)
n_iter, V_iter = convergencia(C, rango_w)

# Gráficos
A = C.get_carga()
fig = plt.figure(1)
plt.clf()
plt.imshow(A, origin='bottom', interpolation='nearest', cmap='gray',
           extent=[-5, 5, -7.5, 7.5])
plt.colorbar()
plt.title('Densidad de carga en el rect'u'á''ngulo')
plt.xlabel('x [cm]')
plt.ylabel('y [cm]')
plt.savefig('carga.eps')

plt.figure(2)
plt.clf()
plt.plot(rango_w, n_iter)
plt.ylim([0, 10000])
plt.ylabel('N'u'ú''mero de iteraciones')
plt.xlabel('$w$')
plt.title('N'u'ú''mero de iteraciones para converger en funci'u'ó''n de w')
plt.savefig('convergencia.eps')

y = C.reticulado * np.array(range(C.Ny)) - 7.5
for n in range(9):
    V = V_iter[n]
    V_y = np.zeros(C.Ny)
    for k in range(C.Ny):
        V_y[k] = V[k][20]

    fig = plt.figure(3)
    plt.clf()
    ax = fig.add_subplot(111)
    ax.plot(y, V_y)
    ax.set_xlabel('y [cm]')
    ax.set_ylabel('V [C]')
    ax.set_title('Perfil lateral del potencial')
    plt.savefig('perfil'+str(int(10 * rango_w[n]))+'.eps')

    plt.figure(4)
    plt.clf()
    plt.imshow(V, origin='bottom', interpolation='nearest',
               extent=[-5, 5, -7.5, 7.5])
    plt.colorbar()
    plt.title('Potencial electrostatico V [C]')
    plt.xlabel('x [cm]')
    plt.ylabel('y [cm]')
    plt.savefig('potencial'+str(int(10 * rango_w[n]))+'.eps')

    plt.figure(5)
    plt.clf()
    plt.imshow(np.arctan(10*V), origin='bottom', interpolation='nearest',
               extent=[-5, 5, -7.5, 7.5])
    plt.colorbar()
    plt.title('$arctan(10*V)$')
    plt.xlabel('x [cm]')
    plt.ylabel('y [cm]')
    plt.savefig('atanpotencial'+str(int(10 * rango_w[n]))+'.eps')
