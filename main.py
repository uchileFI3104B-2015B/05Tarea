
''' Calculo de potencial electrostatico en caja cerrada
de tamano 10 x 15 [cm], reticulado de 0.2 [cm]
uso: solv_poisson.py
'''

import math
import box
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from mpl_toolkits.mplot3d import Axes3D


def fmt(x, pos):
    ''' Funcion para plotear matriz 2-D con paleta de colores
    en notacion cientifica'''
    a, b = '{:.2e}'.format(x).split('e')
    b = int(b)
    return r'${} \times 10^{{{}}}$'.format(a, b)

# Main driver
if __name__ == '__main__':
    # Crear caja vacia de 10 x 15 cm
    box = box.box()

    # Escribir letra F
    box.draw_letter()

    # Escribir condiciones de borde constantes
    box.def_border_conditions(0, 0, 0, 0)

    # Escribir condicion de borde derivativa
    box.def_deritative_conditions(-3, 3, -5.5, -5.5, 1)

    ''' Grafico de cajas en situacion inicial '''

    ''' Caja almacenadora de carga '''
    charge_box = np.array(box.charge_box)
    charge_box = np.transpose(charge_box)
    fig = plt.figure(1)
    ax = fig.add_subplot(121)
    ax.set_title('colorMap')
    plt.imshow(charge_box, extent=[-5, 5, 7.5, -7.5])
    ax.set_aspect('equal')
    plt.colorbar(orientation='vertical', format=ticker.FuncFormatter(fmt))
    plt.gca().invert_yaxis()

    plt.title('Distribucion de carga\n electrica')
    plt.xlabel('Eje x [cm]')
    plt.ylabel('Eje y [cm]')
    plt.grid()

    ''' Caja de voltaje inicial '''
    volt_box_ini = np.array(box.volt_box)
    volt_box_ini = np.transpose(volt_box_ini)
    ax = fig.add_subplot(122)
    ax.set_title('colorMap')
    plt.imshow(volt_box_ini, extent=[-5, 5, 7.5, -7.5])
    ax.set_aspect('equal')
    plt.colorbar(orientation='vertical')
    plt.gca().invert_yaxis()

    plt.title('Distribucion de Voltaje\n antes de integracion')
    plt.xlabel('Eje x [cm]')
    plt.ylabel('Eje y [cm]')
    plt.grid()

    plt.tight_layout()

    # Resolver
    box.solv_poisson(epsilon=0.0005, w=0.8, tolerance=1e-7)

    # Presentar resultados

    ''' Se verifica que la carga sume 1 [C] '''
    print("Carga total = " + str(np.sum(charge_box)) + " [C]")

    ''' Grafico de potencial calculado '''
    volt_box = np.array(box.volt_box)
    volt_box = np.transpose(volt_box)
    fig = plt.figure(2)
    ax.set_title('colorMap')
    plt.imshow(volt_box, extent=[-5, 5, 7.5, -7.5])
    ax.set_aspect('equal')
    plt.colorbar(orientation='vertical')
    plt.gca().invert_yaxis()

    plt.title('Voltaje calculado en la caja\n Permitividad = 5e-4 F/m')
    plt.xlabel('Eje x [cm]')
    plt.ylabel('Eje y [cm]')
    plt.grid()
    plt.show()
