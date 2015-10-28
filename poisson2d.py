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


def una_iteracion(V, V_sgte, Carga, paso, w, linea):
  '''
  Recibe V, V_sgte, Carga, correspondientes a matrices del mismo tamanno,
  paso es el paso en distancias de unidad normalizada, w es el criterio
  para variar la velocidad de convergencia y linea corresponde a si
  hay o no linea dentro de la caja. 
  Devuelve los parametros actualizados.
  '''
  l_x = len(V[0,:])
  l_y = len(V[0,:])
  
  if linea == False:
    for i in range(1, l_x - 1):
      for j in range(1, l_y - 1):
        V_sgte[j,i] = (1 - w) * V[j,i] + w / 4. * (V[j,i+1] + V_sgte[j,i-1] + V[j+1,i] + V_sgte[j-1,i] + paso**2 * Carga[j,i])


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
carga = caja_letra_N(10, 15, 0.25, 1./17.)


box, i = resolvedor(box, box_sgte, carga, 0.25, 1.2, False, 10**5, 10**-7)
print i
graficar(box)

graficar(carga)







