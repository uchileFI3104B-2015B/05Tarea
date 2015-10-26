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

def caja(largo_x, largo_y, paso):
  '''
  Crea una matriz de ceros. El tamaño de la matriz esta determinado por el
  el largo de la caja y el paso con el que se quiere crear la malla. Se
  considerara la division entera de los largos y el paso.
  '''
  return np.zeros( ( int(largo_y/paso) , int(largo_x)/paso ) )
  

  
  
  
  
  
  
  
  
  
  
  
  
