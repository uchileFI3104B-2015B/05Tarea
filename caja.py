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
        self.N_x = int(np.ceil((1.0 * Lx) / h + 1))
        self.N_y = int(np.ceil((1.0 * Ly) / h + 1))
        self.carga = np.zeros((self.N_x, self.N_y))
        self.potencial = np.zeros((self.N_x, self.N_y))
        self.pt_cond_der = {} #diccionario para puntos con condicion derivativa

    def agregar_linea_horizontal(self):
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
