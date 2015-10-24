#######################################################
'''
Metodos Numericos para la Ciencia e Ingenieria
FI3104-1
Tarea 5
Maximiliano Dirk Vega Aguilera
18.451.231-9
'''
#######################################################

import numpy as np
import matplotlib.pyplot as pyplot

#######################################################

#funciones

#######################################################

#construir caja
'''
caja de 10cmx15cm
centro de caja = (0,0)
'''
Lx = 10.           #[cm] largo de la caja en eje x
Ly = 15.           #[cm] largo de la caja en eje y
N = 150            #numero de pasos a dar
hx = Lx / (N - 1)  #tamanho del paso en eje x
hy = Ly / (N - 1)  #tamanho del paso en eje y
h = 1.0            #[cm] tamanho del paso
Nx = (Lx / h) + 1  #numero de pasos a dar en eje x
Ny = (Ly / h) + 1  #numero de pasos a dar en eje y

caja = np.zeros( (Nx , Ny) )  #se construye caja
caja[Nx/2,Ny/2] = 1

#######################################################

#construir letra

#######################################################

#construir condiciiones

#######################################################

#zona de pruebas
print np.transpose(caja)

#######################################################
