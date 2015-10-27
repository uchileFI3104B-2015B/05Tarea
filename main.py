
''' Calculo de potencial electrostatico en caja cerrada
de tamano 10 x 15 [cm], reticulado de 0.2 [cm]
uso: solv_poisson.py
'''

import math
import box
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Main driver
if __name__ == '__main__':
    # Crear caja vacia de 10 x 15 cm
    box = box.box()

    # Escribir letra F
    box.draw_letter()

    # Escribir condiciones de borde constantes
    box.def_border_conditions(0, 0, 0, 0)

    # Escribir condicion de borde derivativa
    box.def_deritative_conditions(-3, 3, -5.5, -5.5, 0.001)

    # Resolver
    box.solv_poisson(epsilon=0.2, w=0.8, tolerance=1e-4)

    # Presentar resultados

    showbox = np.array(box.volt_box)

    fig = plt.figure()

    ax = fig.add_subplot(111)
    ax.set_title('colorMap')
    plt.imshow(showbox)
    ax.set_aspect('equal')
    plt.colorbar(orientation='vertical')
    plt.show()
