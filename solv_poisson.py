
''' Calculo de potencial electrostatico en caja cerrada
de tamano 10 x 15 [cm], reticulado de 0.2 [cm]
uso: solv_poisson.py
'''

import math, box
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
    # Escribir condicion de borde derivativa
    # Resolver
    # Presentar resultados

    showbox = np.array(box.box)

    print(showbox.sum())

    fig = plt.figure()

    ax = fig.add_subplot(111)
    ax.set_title('colorMap')
    plt.imshow(showbox)
    ax.set_aspect('equal')
    plt.colorbar(orientation='vertical')
    plt.show()
