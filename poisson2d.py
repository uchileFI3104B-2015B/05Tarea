#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
#                                    TAREA 5                                   #
################################################################################

'''
Universidad de Chile
Facultad de Ciencias Fisicas y Matematicas
Departamento de Fisica
FI3104 Metodos Numericos para la Ciencia y la Ingenieria
Semestre Primavera 2015

Nicolas Troncoso Kurtovic
'''

import matplotlib.pyplot as p
import numpy             as np

################################################################################
#                                                                              #
################################################################################

'''
Este codigo resuelve la ecuacion de poisson para las condiciones indicadas.
Se utilizan unidades normalizadas.
'''

def caja(largo_x, largo_y, paso):
  '''
  Crea una matriz de ceros. El tamaño de la matriz esta determinado por el
  el largo de la caja y el paso con el que se quiere crear la malla. Se
  considerara la division entera de los largos y el paso.
  '''
  return np.zeros( ( int(largo_y/paso) , int(largo_x)/paso ) )
  

def caja_letra_N(largo_x, largo_y, paso, densidad):
  '''
  Crea una letra N de ancho 1 y densidad de carga constante. La letra tiene
  dimensiones de 5x7  
  '''
  caja_N = caja(largo_x, largo_y, paso)
  pasos_to_1 = 1./paso        #numero de pasos necesarios para avanzar 1
  
  for i in range( int( largo_x / paso ) ):
    if i > (2.5 * pasos_to_1 - 1) and i <= (7.5 * pasos_to_1 -1):
      for j in range( int( largo_y / paso ) ):
        if j > (4 * pasos_to_1 - 1) and j <= (11 * pasos_to_1 -1):
          
          if i <= (3.5 * pasos_to_1 -1):
            caja_N[j][i] = densidad
          elif i <= (4.5 * pasos_to_1 -1):
            if j >= (6 * pasos_to_1 - 1) and j < (7 * pasos_to_1 -1):
              caja_N[j][i] = densidad
          elif i <= (5.5 * pasos_to_1 -1):
            if j >= (7 * pasos_to_1 - 1) and j < (8 * pasos_to_1 -1):
              caja_N[j][i] = densidad
          elif i <= (6.5 * pasos_to_1 -1):
            if j >= (8 * pasos_to_1 - 1) and j < (9 * pasos_to_1 -1):
              caja_N[j][i] = densidad
          else:
            caja_N[j][i] = densidad
  
  return caja_N


def una_iteracion(V, V_sgte, Carga, paso, w, linea):
  '''
  Recibe V, V_sgte, Carga, correspondientes a matrices del mismo tamanno,
  paso es el paso en distancias de unidad normalizada, w es el criterio
  para variar la velocidad de convergencia y linea corresponde a si
  hay o no linea dentro de la caja. 
  El algoritmo resuelve la caja entera si no hay linea, mientras que si
  existe linea se resuelve la caja por trozos dependiendo de las 
  condiciones de borde.
  Devuelve los parametros actualizados.
  '''
  l_x = len(V[0,:])
  l_y = len(V[:,0])
  
  if linea == False:  # Para el caso en que no hay linea
    for i in range(1, l_x - 1):
      for j in range(1, l_y - 1):
        V_sgte[j,i] = (1 - w) * V[j,i] + w / 4. * ( V[j,i+1] + V_sgte[j,i-1]
                                                  + V[j+1,i] + V_sgte[j-1,i]
                                                  + paso**2 * Carga[j,i] )
  
  else: 
    linea = int(13. / paso)
    a = int(2. / paso)
    b = int(8. / paso)
    for i in range(1, l_x-  1): # Parte superior de la caja, contiene la letra
      for j in range(1, linea - 1):
        V_sgte[j,i] = (1 - w) * V[j,i] + w / 4. * ( V[j,i+1] + V_sgte[j,i-1]
                                                  + V[j+1,i] + V_sgte[j-1,i]
                                                  + paso**2 * Carga[j,i] )

    for i in range(a, b): # Sobre la linea
      V_sgte[linea-1,i] = (1 - w) * V[linea-1,i] + w / 3. * ( V[linea - 1, i+1]
                                     + V_sgte[linea - 1, i-1]
                                     + V_sgte[linea - 2, i]
                                     - paso + paso**2 * Carga[j,i] )

    for i in range(a, b): # En la linea
      V_sgte[linea,i] = V[linea - 1, i] + paso  # condicion g=1

    for i in range(a, b): # Bajo la linea
      V_sgte[linea+1,i] = (1 - w) * V[linea+1,i] + w / 3. * ( V[linea + 1, i+1]
                                     + V_sgte[linea + 1, i-1]
                                     + V_sgte[linea + 2, i]
                                     + paso + paso**2 * Carga[j,i] )

    for i in range(b , l_x - 1): # Parte lateral derecha de la linea
      for j in range(linea - 1 , linea + 2):
        V_sgte[j,i] = (1 - w) * V[j,i] + w / 4. * ( V[j,i+1] + V_sgte[j,i-1]
                                                  + V[j+1,i] + V_sgte[j-1,i]
                                                  + paso**2 * Carga[j,i] )

    for i in range(1, a): # Parte lateral izquierda de la linea
      for j in range(linea - 1 , linea + 2):
        V_sgte[j,i] = (1 - w) * V[j,i] + w / 4. * ( V[j,i+1] + V_sgte[j,i-1]
                                                  + V[j+1,i] + V_sgte[j-1,i]
                                                  + paso**2 * Carga[j,i] )

    for i in range(1, l_x - 1): # Parte baja de la caja
      for j in range(linea + 2, l_y -1):
        V_sgte[j,i] = (1 - w) * V[j,i] + w / 4. * ( V[j,i+1] + V_sgte[j,i-1]
                                                  + V[j+1,i] + V_sgte[j-1,i]
                                                  + paso**2 * Carga[j,i] )

    

def no_ha_convergido(V, V_sgte, tolerancia = 10**-5):
    '''
    Compara el potencial actual con el del paso anterior y determina si
    ha convergido o no a partir de nuestra tolerancia.
    '''
    not_zero = (V_sgte != 0)
    diff_relativa = (V - V_sgte)[not_zero] / V_sgte[not_zero]
    max_diff = np.max(np.fabs(diff_relativa))
    if max_diff > tolerancia:
        return True
    else:
        return False


def resolvedor(V, V_sgte, Carga, paso, w, linea, N, tol):
  '''
  Resuelve un sistema utilizando la funcion una_interacion hasta que
  converja segun una tolerancia 'tol' o hasta realizar N iteraciones.
  '''
  una_iteracion(V, V_sgte, Carga, paso, w, linea)
  i = 1
  while i < N and no_ha_convergido(V, V_sgte, tol):
    V = V_sgte.copy()
    una_iteracion(V, V_sgte, Carga, paso, w, linea)
    i += 1
  return V, i
  
  
def graficar(V):
  '''
  Grafica la matriz V
  '''
  p.imshow(np.arcsinh(V) , interpolation = 'nearest',
    extent=[-5, 5, -7.5, 7.5])
  p.xlabel('X $[cm]$')
  p.ylabel('Y $[cm]$')
  p.colorbar()
  p.show()  


################################################################################
#                                                                              #
################################################################################

box = caja(10, 15, 0.25)
box_sgte = caja(10, 15, 0.25)
density = 1./(17.*16.)  # densidad de carga
h = 0.25
carga = caja_letra_N(10, 15, 0.25, 1.)
ww = 1.8     # parametro w
tolerancia = 10**-7
iter_max = 10** 5


box1, i1 = resolvedor(box, box_sgte, carga, h, ww, False, iter_max, tolerancia)
print i1
graficar(box1)

graficar(carga)

box2, i2 = resolvedor(box, box_sgte, carga, h, ww, True, iter_max, tolerancia)
print i2
graficar(box2)


ww = 1.2

box3, i3 = resolvedor(box, box_sgte, carga, h, ww, True, iter_max, tolerancia)
print i3
graficar(box3)


box4 = box3-box1
graficar(box4)

