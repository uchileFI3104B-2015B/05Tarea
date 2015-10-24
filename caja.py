#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        self.pt_cond_der = {} #diccionario para puntos con condicion derivativa
        self.indices_lineas_horizontal = []

    def agregar_linea_horizontal(self, x_c=0, y_c=-5.5, L=6, dV=1):
        h = self.reticulado
        N_puntos = int(L / h + 1)
        i_0 = int((x_c + (self.Lx - L) / 2.0) / h)
        j_0 = int((y_c + self.Ly / 2.0) / h)
        self.indices_lineas_horizontal.append(j_0)
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
        #Límites de la letra
        i_min, i_max, j_min, j_inter, j_max = (13, 37, 21, 36, 54)
        #Densidad asociada [C/cm^2]
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
        pass

    def pasada_sobre_relajacion(self, w, region):
        pass

    def relaja(self, w, N_pasadas):
        pass

    def get_potencial(self):
        pass

    def get_carga(self):
        carga = np.zeros((self.N_y, self.N_x))
        for i in range(self.N_x):
            for j in range(self.N_y):
                carga[j][i] = self.carga[i][j]
        return carga
