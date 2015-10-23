#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FixedLocator, FormatStrFormatter
import pdb

ANCHO = 10.+1
ALTO = 15.+1
H = 0.2

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


def poner_carga(caja,carga,total):
    '''recibe la caja a modificar, la carga total a colocar y
     las coordenadas para setear el arreglo de cargas inicial '''
    carga_en_un_punto = total / len(carga)
    for par in carga:
        caja[par[1],par[0]] = carga_en_un_punto
    return caja


def iteracion_zona_1():
    '''avanza el algoritmo de sobre relajación 1 vez, en la zona 1 (fuera del
    cuadrado de la letra, y lejos de la linea)'''


def iteracion_zona_2():
    '''avanza el algoritmo de sobre relajación 1 vez, en la zona 2 (detnro del
    cuadrado de laletra)'''


def iteracion_zona_3():
    '''avanza el algoritmo de sobre relajación 1 vez, en la zona 3 (cerca
    de la linea)'''


def converge():
    '''compara 2 estados de la malla, y decide si converge según la tolerancia
    pedida'''


def f_caja_carga(x,y):
    '''función auxilar para plotear, recibe la coordenada x e y y devuelve
    el valor de la malla de carga en esas coordenadas'''
    return caja_carga[y,x]


def f_caja_potencial(x,y):
    '''función auxilar para plotear, recibe la coordenada x e y y devuelve
    el valor de la malla de potencial en esas coordenadas'''
    return caja_potencial[y,x]


def mostrar(f_caja,caja,titulo):
    '''plotea la solución en 3D'''
    #pdb.set_trace()
    (alto,ancho) = caja.shape
    x = np.linspace(0,ancho-1,ancho)
    y = np.linspace(0,alto-1,alto)

    xg, yg = np.meshgrid(x, y)

    vector_f = np.vectorize(f_caja)
    z = vector_f(xg,yg)


    fig = plt.figure()
    ax = fig.gca(projection='3d')
    plt.title(titulo)
    #ax.plot_surface(xg, yg, z, rstride=1, cstride=1, cmap=cm.coolwarm,
    #    linewidth=0, antialiased=False)
    surf = ax.plot_surface(xg, yg, z, rstride=1, cstride=1,
                           linewidth=0, antialiased=False, shade=False)



    def es_horizontal(ini, fin):
        '''retorna true si el traso es horizontal, o false si es vertical'''
        return (ini[0]==fin[0])


    def trazo(ini,fin,ancho):
        '''recibe la coordenada de inicio del trazo, el final y el ancho del
        trazo, devuelve un arregl con las coordenadas de los puntos que lo
        conformman. Sólo funciona para trazos rectos.
        (recibe los puntos más izquierdos, o más  abajo del trazo)'''
        actual = ini
        trazo = np.array([])
        if es_horizontal(ini,fin):
            paso = np.array([0,1])
            ancho_1 = np.array([0,ancho])
        else:
            paso = np.array([1,0])
            ancho_1 = np.array([0,ancho])
        for a in range(ancho)


        return trazo


    def armar_letra():
        '''devuelve el arreglo de coordenaas que conforman la letra'''
        ini = np.array([])
        fin = np.array([])
        ancho = 1
        trazo_1 = trazo(ini, fin , ancho)

        ini2 = np.array([])
        fin2 = np.array([])
        trazo_2 = trazo(ini2,fin2,ancho)

        letra = [trazo_1,trazo_2]
        return letra


#main
#pdb.set_trace()
carga = armar_letra()
carga_total = 1.

caja_carga = crear_caja(ANCHO,ALTO,H)
caja_potencial = crear_caja(ANCHO,ALTO,H)


caja_carga = poner_carga(caja_carga,carga,carga_total)

'''
caja = poner_condiciones_borde()
caja = poner_linea()

while(i<20)
    caja = iteración_zona_1()
    caja = iteración_zona_2()
    caja = iteración_zona_3()
    if converge():
        break

print("numero iteraciones = "+str(i))
'''
mostrar(f_caja_carga,caja_carga,"distribucion carga")
mostrar (f_caja_potencial,caja_potencial,"potencial")
plt.show()
