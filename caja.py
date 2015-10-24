#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

class Caja(object):
    def __init__(self, Lx=10, Ly=15, h=0.2):
        '''
        Inicializa caja vacía
        '''
        self.reticulado = 1.0 * h
        self.largo_x = 1.0 * Lx
        self.largo_y = 1.0 * Ly
        self.N_x = int((1.0 * Lx) / h + 1)
        self.N_y = int((1.0 * Ly) / h + 1)
        self.carga = np.zeros((self.N_x, self.N_y))
        self.potencial = np.zeros((self.N_x, self.N_y))
        self.pt_cond_der = {} #diccionario para puntos con condicion derivativa
        self.indices_lineas_horizontal = []

    def agregar_linea_horizontal(self, x_c=0, y_c=-5.5, L=6, dV=1):
        h = self.reticulado
        Lx = self.largo_x
        Ly = self.largo_y
        N_puntos = int(L / h + 1)
        i_0 = int((x_c + (Lx - L) / 2.0) / h)
        j_0 = int((y_c + Ly / 2.0) / h)
        self.indices_lineas_horizontal.append(j_0)
        for k in range(N_puntos):
            i = i_0 + k
            self.pt_cond_der[(i, j_0)] = dV
        pass

    def agregar_letra_B(self):
        pass

    def adyacente_linea_horizontal(self, i, j):
        pass

    def paso_sobre_relajacion(self, i, j, w, region):
        pass

    def pasada_sobre_relajacion(self, w, region):
        pass

    def relaja(self, w, N_pasadas):
        pass

    def get_potencial(self):
        pass

    def get_carga(self):
        pass
