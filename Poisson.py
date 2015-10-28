# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 19:41:28 2015
Este programa calcula el potencial dentro de una caja de 10x15
que contiene la letra "B" que tiene una carga de 1[C],
usando la ecuación de Poisson.
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import pdb

# Condiciones iniciales

L_x = 10
L_y = 15
h = 0.2

#Funciones

def crear_caja(x, y, h):
    '''Recibe las dimensiones de la caja  y el tamaño del reticulado
     y la inicia en ceros '''
    ancho_efectivo = x / h + 1
    largo_efectivo = y / h + 1
    caja = np.zeros((ancho_efectivo, largo_efectivo))

    return caja

def poner_condiciones_borde(caja):
    '''Conecta a tierra el perímetro de la caja, la segunda iteración
    (bordes laterales) se itera desde borde+1, hasta borde para evitar pasar
    2 veces por las esquinas'''
    borde_inferior = np.array([np.array([-5, -7.5]), np.array([5, -7.5])])
    borde_superior = np.array([np.array([-5, 7.5]), np.array([5, 7.5])])
    borde_inferior[0] = transformar(borde_inferior[0])
    borde_inferior[1] = transformar(borde_inferior[1])
    borde_superior[0] = transformar(borde_superior[0])
    borde_superior[1] = transformar(borde_superior[1])
    for i in range(int(borde_inferior[0][0]), int(borde_inferior[1][0]) + 1):
        caja[i, borde_inferior[0][1]] = 0
        caja[i, borde_superior[0][1]] = 0
    for i in range(int(borde_inferior[0][1])+1, int(borde_superior[0][1])):
        caja[borde_inferior[0][0], i] = 0
        caja[borde_superior[1][0], i] = 0
    return caja
    
def transformar(coordenada):
    ''' Recibe coordenadas considerando 0,0 como el centro y
    las dimensiones originales en centímetros, a las unidades de la grilla
     (Notar que se utiliza Ancho+1 porque el arreglo se define desde 0)'''

    x, y = coordenada[0], coordenada[1]
    x_tran = int((x + (L_x)/2)/h)
    y_tran = int((y + (L_y)/2)/h)
    return x_tran, y_tran
    
def es_horizontal(ini, fin):
        '''Retorna true si el trazo es horizontal, false si es vertical'''
        return (ini[1] == fin[1])


def trazo(ini, fin, ancho):
    '''Recibe la coordenada de inicio del trazo, el final y el ancho del
    trazo, devuelve un arreglo con las coordenadas de los puntos que lo
    conformman. Sólo funciona para trazos rectos.
    (recibe los puntos más izquierdos, o más  abajo del trazo)'''
    ancho = int(ancho)+1
    actual = ini
    if es_horizontal(ini, fin):
        paso = np.array([1, 0])
        ancho_1 = np.array([0, 1])
        rango = int(np.fabs(fin[0]-ini[0]))+1
    else:
        paso = np.array([0, 1])
        ancho_1 = np.array([1, 0])
        rango = int(np.fabs(fin[1]-ini[1]))

    trazo = np.zeros([(rango)*(ancho), 2])
    for a in range(ancho):
        for i in range(rango):
            trazo[i+(rango)*a] = np.array([actual])
            actual += paso
        actual = ini
        actual += (a+1)*ancho_1
    
    return trazo


def dentro_letra_B(x, y):
    '''Devuelve True si la coordenada está dentro del bloque que contiene
    la letra'''
    if (2.5 / h <= x and x <= 7.5 / h):
        if(4 / h <= y and y <= 11 / h):
            return True
    return False
    
def armar_letra_B():
    '''Devuelve el arreglo de coordenaas que conforman la letra B, las coordenadas
     ini y fin se dan considerando 0,0 en el centro y
     las dimensiones en centímetros'''
    ancho = 1
    ini = np.array([-2.5, -3.5])
    fin = np.array([-2.5, 3.5])
    ini2 = np.array([-1.5, 2.5])
    fin2 = np.array([1.5, 2.5])
    ini3 = np.array([-1.5, -0.5])
    fin3 = np.array([1.5, -0.5])
    ini4 = np.array([-1.5, -3.5])
    fin4 = np.array([1.5, -3.5])
    ini5 = np.array([1.5, 0.5])
    fin5 = np.array([1.5, 2.5])
    ini6 = np.array([1.5, -2.5])
    fin6 = np.array([1.5, -0.5])

    ancho_transf = ancho / h
    ini, fin = transformar(ini), transformar(fin)
    ini2, fin2 = transformar(ini2), transformar(fin2)
    ini3, fin3 = transformar(ini3), transformar(fin3)
    ini4, fin4 = transformar(ini4), transformar(fin4)
    ini5, fin5 = transformar(ini5), transformar(fin5)
    ini6, fin6 = transformar(ini6), transformar(fin6)

    trazo_1 = trazo(ini, fin, ancho_transf)
    trazo_2 = trazo(ini2, fin2, ancho_transf)
    trazo_3 = trazo(ini3, fin3, ancho_transf)
    trazo_4 = trazo(ini4, fin4, ancho_transf)
    trazo_5 = trazo(ini5, fin5, ancho_transf)
    trazo_6 = trazo(ini6, fin6, ancho_transf)
    letra = np.append(trazo_1, trazo_2, axis=0)
    letra = np.append(letra, trazo_3, axis=0)
    letra = np.append(letra, trazo_4, axis=0)
    letra = np.append(letra, trazo_5, axis=0)
    letra = np.append(letra, trazo_6, axis=0)
    return letra
    
def esta_bajo_linea(i, j):
    '''Devuele true si la coordenada es inmediatamente bajo la linea '''
    if (j == 2 / h - 1):
        if(2 / h <= i and i <= 8 / h):
            return True
    return False


def esta_sobre_linea(i, j):
    '''Devuelve true si la coordenada esta sobre la linea con condiciones
    derivativas'''
    if(j == 2 / h + 1):
        if(2 / h <= i and i <= 8 / h):
            return True
    return False


def esta_en_linea(i, j):
    '''Devuelve true si la coordenada pertenece a la linea'''
    if(j == 2 / h):
        if(2 / h <= i and i <= 8 / h):
            return True
    return False

def Iteracion(caja, caja_next, caja_carga, numero_pasos, h, w=1):
    '''Avanza el algoritmo de sobre relajación y llama a la iteración
    correspondiente para cada coordenada.
    '''
    rango_x = np.array([0 / h, 10 / h])
    rango_y = np.array([0 / h, 15 / h])
    for i in range(int(rango_x[0]) + 1, int(rango_x[1])):
        for j in range(int(rango_y[0]) + 1, int(rango_y[1])):
            if (esta_bajo_linea(i, j)):
                iteracion_bajo_linea(i, j, caja, caja_next, caja_carga,
                                     numero_pasos, h, w=1)
            elif esta_en_linea(i, j):
                iteracion_linea(i, j, caja, caja_next, caja_carga,
                                numero_pasos, h, w=1)
            elif esta_sobre_linea(i, j):
                iteracion_sobre_linea(i, j, caja, caja_next, caja_carga,
                                      numero_pasos, h, w=1)
            elif (dentro_letra_B(i, j)):
                iteracion_letra(i, j, caja, caja_next, caja_carga,
                                numero_pasos, h, w=1)
            else:
                iteracion_resto(i, j, caja, caja_next, caja_carga,
                                numero_pasos, h, w=1)


def iteracion_resto(i, j, caja, caja_next, caja_carga, numero_pasos, h, w=1):
    '''avanza el algoritmo de sobre relajación 1 vez, fuera del rectangulo
    interior y lejos de la linea'''
    caja_next[i, j] = ((1 - w) * caja[i, j] +
                       w / 4 * (caja[i + 1, j] + caja_next[i - 1, j] +
                                caja[i, j+1] + caja_next[i, j-1]))


def iteracion_letra(i, j, caja, caja_next, caja_carga, numero_pasos, h, w=1):
    '''avanza el algoritmo de sobre relajación 1 vez, en el casillero interior
    que contiene la letra'''
    caja_next[i, j] = ((1 - w) * caja[i, j] +
                       w / 4 * (caja[i+1, j] + caja_next[i-1, j] +
                                caja[i, j+1] + caja_next[i, j-1] +
                                h**2 * caja_carga[i, j]))


def iteracion_linea(i, j, caja, caja_next, caja_carga, numero_pasos, h, w=1):
    '''evalua el potencial en la linea con la condición de que la derivada
    debe ser 1'''
    caja_next[i, j] = caja_next[i, j-1] + h


def iteracion_bajo_linea(i, j, caja, caja_next, caja_carga,
                         numero_pasos, h, w=1):
    '''avanza el algoritmo de sobre relajación 1 vez en los
    casilleros inferiores vecinos a la linea'''
    y = 2 / h - 1
    caja_next[i, y] = ((1-w)*caja[i, y] + w/3*(caja_next[i-1, y] +
                                               caja[i+1, y] +
                                               caja_next[i, y-1] + h))


def iteracion_sobre_linea(i, j, caja, caja_next, caja_carga,
                          numero_pasos, h, w=1):
    '''avanza el algoritmo de sobre relajación 1 vez en los
    casilleros superiores vecinos a la linea'''
    y = 2 / h + 1
    caja_next[i, y] = ((1-w)*caja[i, y] + w/3*(caja_next[i-1, y] +
                                               caja[i+1, y] +
                                               caja_next[i, y+1] - h))

def no_converge(V, V_next, tolerancia):
    ''' Devuelve True si es que la iteracion converge'''
    not_zero = (V_next != 0)
    diff_relativa = (V - V_next)[not_zero] / V_next[not_zero]
    max_diff = np.max(np.fabs(diff_relativa))
    if max_diff > tolerancia:
        return True
    else:
        return False
        
def poner_carga(caja, coordenadas):
    '''recibe la caja a modificar, la carga total a colocar y
     las coordenadas para setear el arreglo de cargas inicial '''
    carga_en_un_punto = 1 / len(coordenadas)
    for par in coordenadas:
        caja[par[0], par[1]] = carga_en_un_punto
    return caja
    
def f_carga_caja(x, y):
    '''función auxilar para graficar'''
    return carga_caja[x, y]


def f_V_next(x, y):
    '''función auxilar para graficar'''
    return V_next[x, y]
    
def mostrar(f_caja, caja, titulo):
    '''plotea la solución en 3D'''
    x_original = [0, 2.5, 5, 7.5, 10]
    y_original = [0, 3, 6, 9, 12, 15]
    x_scale = [0, 12.5, 25, 37.5, 50]
    y_scale = [0, 15, 30, 45, 60, 75]
    (ancho, alto) = caja.shape
    x = np.linspace(0, ancho-1, ancho)
    y = np.linspace(0, alto-1, alto)
    xg, yg = np.meshgrid(x, y)
    vector_f = np.vectorize(f_caja)
    z = vector_f(xg, yg)
    
    fig = plt.figure(1)
    fig.clf()
    ax = fig.add_subplot(111)
    cax = ax.imshow(z, origin='bottom', interpolation='nearest')
    ax.contour(z, origin='lower')
    ax.set_title(titulo)
    ax.set_xticks(x_scale)
    ax.set_xticklabels(x_original)
    ax.set_yticks(y_scale)
    ax.set_yticklabels(y_original)
    ax.set_xlabel("X [cm]")
    ax.set_ylabel("Y [cm]")
    cbar = fig.colorbar(cax)
    
    if titulo == "valor del potencial":
        cbar.set_label("Potencial [erg/C]")
        fig.savefig("potencial.jpg")
    else:
        cbar.set_label("Carga [C]")
        fig.savefig("distr_carga.jpg")

#Main

#Inicializacion

w=1.2
N_pasos = np.array([(L_x/h) + 1, (L_y/h) + 1])
coordenadas_carga = armar_letra_B()

carga_caja = crear_caja(L_x, L_y, h)
V_actual = crear_caja(L_x, L_y, h)
V_next = crear_caja(L_x, L_y, h)

carga_caja = poner_carga(carga_caja, coordenadas_carga)

V_actual = poner_condiciones_borde(V_actual)


#Iteracion

Iteracion(V_actual, V_next, carga_caja, N_pasos, h, w)
contador = 1
tolerancia = 1e-1
while (contador < 500 and no_converge(V_actual, V_next, tolerancia)):
    V_actual = V_next.copy()
    Iteracion(V_actual, V_next, carga_caja, N_pasos, h, w)
    contador += 1
    
#Resultados
    
print("numero iteraciones: "+str(contador))

mostrar(f_carga_caja, carga_caja, "distribucion carga")
mostrar(f_V_next, V_next, "valor del potencial")
plt.show()

