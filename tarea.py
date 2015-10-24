#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import pdb

ANCHO = 10
ALTO = 15
H = 0.2

def crear_caja(ancho , alto, h):
    '''recibe las dimensiones de la caja  y el tamaño del reticulado
     y la inicia en puros ceros '''
    ancho_efectivo = ancho/h +1
    alto_efectivo = alto/h +1
    caja = np.zeros ((ancho_efectivo,alto_efectivo) )

    return caja


def poner_condiciones_borde(caja , condiciones):
    '''recibe un arrreglo para las condiciones de borde y las reemplaza en la
    posición respectiva de la caja'''


def poner_linea(caja , condiciones):
    '''recibe un arreglo con las coordenadas para condiciones de borde
    derivativas y sus valores, y las implementa en la caja'''



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
    return caja_carga[x,y]


def f_caja_potencial(x,y):
    '''función auxilar para plotear, recibe la coordenada x e y y devuelve
    el valor de la malla de potencial en esas coordenadas'''
    return caja_potencial[x,y]


def mostrar(f_caja,caja,titulo):
    '''plotea la solución en 3D'''
    (ancho,alto) = caja.shape
    x = np.linspace(0,ancho-1,ancho)
    y = np.linspace(0,alto-1,alto)
    xg, yg = np.meshgrid(x, y)
    vector_f = np.vectorize(f_caja)
    z = vector_f(xg,yg)
    '''
    fig = plt.figure()
    fig.clf()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(xg,yg,z, rstride=1, cstride=1)'''
    fig2 = plt.figure()
    fig2.clf()
    ax2 = fig2.add_subplot(111)
    ax2.imshow(z, origin='bottom', interpolation='nearest')
    ax2.contour(z, origin='lower')

def es_horizontal(ini, fin):
        '''retorna true si el trazo es horizontal, o false si es vertical'''
        return (ini[1]==fin[1])


def trazo(ini,fin,ancho):
    '''recibe la coordenada de inicio del trazo, el final y el ancho del
    trazo, devuelve un arreglo con las coordenadas de los puntos que lo
    conformman. Sólo funciona para trazos rectos.
    (recibe los puntos más izquierdos, o más  abajo del trazo)'''
    ancho = int(ancho)+1
    actual = ini
    if es_horizontal(ini,fin):
        paso = np.array([1,0])
        ancho_1 = np.array([0,1])
        rango = int(np.fabs(fin[0]-ini[0]))+1
    else:
        paso = np.array([0,1])
        ancho_1 = np.array([1,0])
        rango = int(np.fabs(fin[1]-ini[1]))

    trazo = np.zeros([(rango)*(ancho),2])
    for a in range(ancho):
        for i in range(rango):
             trazo[i+(rango)*a] = np.array([actual])
             actual += paso
        actual = ini
        actual += (a+1)*ancho_1

    return trazo


def transformar(coordenada):
    ''' recibe coordenadas considerando 0,0 como el centro y
    las dimensiones originales en centímetros, a las unidades de la grilla
    . Notar que se utiliza Ancho+1 porque el arreglo se define desde 0'''
    x,y = coordenada[0],coordenada[1]
    x_tran = (x + (ANCHO)/2)/H
    y_tran = (y + (ALTO)/2)/H
    return x_tran,y_tran


def armar_letra():
    '''devuelve el arreglo de coordenaas que conforman la letra, las coordenadas
     ini y fin se dan considerando 0,0 en el centro y
     las dimensiones en centímetros'''
    ancho = 1
    ini = np.array([1,-3.5])
    fin = np.array([1,3.5])
    ini2 = np.array([-2,-3.5])
    fin2 = np.array([1,-3.5])

    ancho_transf = ancho /H
    ini,fin = transformar(ini),transformar(fin)
    ini2,fin2 = transformar(ini2),transformar(fin2)

    trazo_1 = trazo(ini, fin ,ancho_transf)
    trazo_2 = trazo(ini2,fin2,ancho_transf)
    letra = np.append(trazo_1,trazo_2,axis=0)
    return letra


def poner_carga(caja,coordenadas,total):
    '''recibe la caja a modificar, la carga total a colocar y
     las coordenadas para setear el arreglo de cargas inicial '''
    carga_en_un_punto = total / len(coordenadas)
    for par in coordenadas:
        caja[par[0],par[1]] = carga_en_un_punto
    return caja


#main
coordenadas_carga = armar_letra()
carga_total = 1.

caja_carga = crear_caja(ANCHO,ALTO,H)
caja_potencial = crear_caja(ANCHO,ALTO,H)

caja_carga = poner_carga(caja_carga,coordenadas_carga,carga_total)

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
