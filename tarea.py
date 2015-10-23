#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FixedLocator, FormatStrFormatter
import pdb

ANCHO = 3.+1
ALTO = 4.+1
H = 1

def crear_caja(ancho , alto, h):
    '''recibe las dimensiones de la caja  y el tamaño del reticulado
     y la inicia en puros ceros '''
    ancho_efectivo = ancho/h
    alto_efectivo = alto/h
    caja = np.zeros ((alto_efectivo,ancho_efectivo) )

    return caja


def poner_condiciones_borde(caja , condiciones):
    '''recibe un arrreglo para las condiciones de borde y las reemplaza en la
    posición respectiva de la caja'''


def poner_linea(caja , condiciones):
    '''recibe un arreglo con las coordenadas para condiciones de borde
    derivativas y sus valores, y las implementa en la caja'''


def poner_carga():
    '''recibe las coordenadas para setear el arreglo de cargas inicial '''


def hacer_una_iteracion():
    '''avanza el algoritmo de sobre relajación 1 vez'''


def converge():
    '''compara 2 estados de la malla, y decide si converge según la tolerancia
    pedida'''


def f(x,y):
    '''función auxilar para plotear, recibe la coordenada x e y y devuelve
    el valor de la malla en esas coordenadas'''
    return caja[y,x]


def mostrar(caja):
    '''plotea la solución en 3D'''
    #pdb.set_trace()
    (alto,ancho) = caja.shape
    x = np.linspace(0,ancho-1,ancho)
    y = np.linspace(0,alto-1,alto)

    xg, yg = np.meshgrid(x, y)

    vector_f = np.vectorize(f)
    z = vector_f(xg,yg)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    #ax.plot_surface(xg, yg, z, rstride=1, cstride=1, cmap=cm.coolwarm,
    #    linewidth=0, antialiased=False)
    surf = ax.plot_surface(xg, yg, z, rstride=1, cstride=1,
                           linewidth=0, antialiased=False, shade=False)
    plt.show()
#main
#pdb.set_trace()
caja = crear_caja(ANCHO,ALTO,H)
'''
caja = poner_condiciones_borde()
caja = poner_linea()
caja = poner_carga()

while(i<20)
    caja = hacer_una_iteracion()
    if converge():
        break

print("numero iteraciones = "+str(i))
'''
mostrar(caja)
