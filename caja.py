#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Este archivo implementa la clase Caja, que contiene dentro de sí una
distribución de carga y tiene definido un potencial electrostático. Tiene
métodos implementados para agregar una línea horizontal con condición
derivativa y una distribución de carga predefinida. Dispone además de métodos
para relajar el sistema hacia la solución de la ecuación de Poisson.
'''

import numpy as np


class Caja(object):
    def __init__(self, Lx=10, Ly=15, h=0.2):
        '''
        Inicializa caja vacía
        '''
        self.reticulado = 1.0 * h
        self.Lx = 1.0 * Lx
        self.Ly = 1.0 * Ly
        self.Nx = int((1.0 * Lx) / h + 1)
        self.Ny = int((1.0 * Ly) / h + 1)
        self.carga = np.zeros((self.Nx, self.Ny))
        self.potencial = np.zeros((self.Nx, self.Ny))
        # diccionario para puntos con condicion derivativa
        self.pt_cond_der = {}
        self.indice_linea = -1

    def agregar_linea_horizontal(self, x_c=0, y_c=-5.5, L=6, dV=1):
        h = self.reticulado
        N_puntos = int(L / h + 1)
        i_0 = int((x_c + (self.Lx - L) / 2.0) / h)
        j_0 = int((y_c + self.Ly / 2.0) / h)
        self.indice_linea = j_0
        for k in range(N_puntos):
            i = i_0 + k
            self.pt_cond_der[(i, j_0)] = dV
        pass

    def agregar_letra_B(self):
        h = self.reticulado
        if not (self.Lx == 10 and self.Ly == 15 and h == 0.2):
            print "Método para agregar letra B a la caja solamente está",
            print "implementado para las dimensiones por defecto."
            return
        # Límites de la letra
        i_min, i_max, j_min, j_inter, j_max = (13, 37, 21, 36, 54)
        # Densidad asociada [C/cm^2]
        area_verticales = 2 * (j_max - j_min + 1) * h
        area_transversales = 3 * (i_max - i_min - 9) * h
        dens = 1.0/(area_verticales + area_transversales)
        for j in range(j_min, j_max + 1):
            for i in range(5):
                self.carga[i + i_min][j] = dens
                self.carga[i + i_max - 4][j] = dens
        for i in range(i_min+5, i_max - 4):
            for j in range(5):
                self.carga[i][j + j_min] = dens
                self.carga[i][j + j_inter] = dens
                self.carga[i][j + j_max - 4] = dens
        pass

    def adyacente_linea_horizontal(self, i, j):
        if (i, j - 1) in self.pt_cond_der.keys():
            return True
        elif (i, j + 1) in self.pt_cond_der.keys():
            return True
        else:
            return False

    def paso_sobre_relajacion(self, i, j, w, region):
        '''
        Este método permite actualizar el valor de la posición (i,j) en la
        grilla según el tipo de condición que debe satisfacer. Además recibe
        como parámetro el valor de w y la región sobre la cual se debe relajar
        la solución.
        '''
        h = self.reticulado
        # Si se está sobre un punto con condición de borde derivativa
        if (i, j) in self.pt_cond_der.keys():
            dV = self.pt_cond_der[(i, j)]
            if region == "up":
                self.potencial[i][j] = self.potencial[i][j+1] - dV * h
            else:
                self.potencial[i][j] = self.potencial[i][j-1] + dV * h
        # Si se está en un punto adyacente a uno con condición de borde
        # derivativa
        elif self.adyacente_linea_horizontal(i, j):
            P0 = self.potencial[i][j] * (1.0 - w)
            P1 = self.potencial[i-1][j]
            P2 = self.potencial[i+1][j]
            if region == "up":
                P3 = self.potencial[i][j+1]
                P4 = - h * self.pt_cond_der[(i, j-1)]
            else:
                P3 = self.potencial[i][j-1]
                P4 = h * self.pt_cond_der[(i, j+1)]
            P5 = h**2 * self.carga[i][j]
            self.potencial[i][j] = P0 + w * (P1 + P2 + P3 + P4 + P5)/3.0
        # Si se está en un punto cualquiera
        else:
            P0 = self.potencial[i][j] * (1.0 - w)
            P1 = self.potencial[i-1][j]
            P2 = self.potencial[i+1][j]
            P3 = self.potencial[i][j-1]
            P4 = self.potencial[i][j+1]
            P5 = h**2 * self.carga[i][j]
            self.potencial[i][j] = P0 + w * (P1 + P2 + P3 + P4 + P5)/4.0
        pass

    def pasada_sobre_relajacion(self, w, region):
        if region == "up":
            for j in range(self.Ny - 2, self.indice_linea - 1, -1):
                for i in range(1, self.Nx - 1):
                    self.paso_sobre_relajacion(i, j, w, region)
        elif region == "down":
            for j in range(1, self.indice_linea + 1):
                for i in range(1, self.Nx - 1):
                    self.paso_sobre_relajacion(i, j, w, region)
        # Si no se especifica una región, entonces se asume que se quiere
        # iterar sobre todo el rectángulo (salvo el perímetro, que se mantiene
        # a valor constante).
        else:
            for j in range(1, self.Ny - 1):
                for i in range(1, self.Nx - 1):
                    self.paso_sobre_relajacion(i, j, w, region)
        pass

    def relaja(self, w, N_pasadas):
        counter = 0
        while counter < N_pasadas:
            self.pasada_sobre_relajacion(w, "up")
            self.pasada_sobre_relajacion(w, "down")
            counter += 1
        pass

    def get_potencial(self):
        potencial = np.zeros((self.Ny, self.Nx))
        for i in range(self.Nx):
            for j in range(self.Ny):
                potencial[j][i] = self.potencial[i][j]
        return potencial

    def get_carga(self):
        carga = np.zeros((self.Ny, self.Nx))
        for i in range(self.Nx):
            for j in range(self.Ny):
                carga[j][i] = self.carga[i][j]
        return carga

    def resetea_potencial(self):
        self.potencial = np.zeros((self.Nx, self.Ny))
        pass
