#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
ANCHO = 10
ALTO = 15

def crear_caja(ancho , alto, h):
    '''recibe las dimensiones de la caja  y el tamaño del reticulado
     y la inicia en puros ceros '''


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

def mostrar():
    '''imprime el arreglo en consola'''

#main
caja = crear_caja()
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
mostrar()
