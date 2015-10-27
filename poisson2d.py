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

import matplotlib.pyplot as     p
import numpy             as     np
from   scipy.integrate   import ode
from   scipy.optimize    import root
from   scipy.optimize    import curve_fit

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

print caja_letra_N(10,15,0.5,1)

