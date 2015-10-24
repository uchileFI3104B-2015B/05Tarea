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
h = 0.5            #[cm] tamanho del paso
Nx = (Lx / h) + 1  #numero de pasos a dar en eje x
Ny = (Ly / h) + 1  #numero de pasos a dar en eje y

caja = np.zeros( (Nx , Ny) )  #se construye caja

'''
busca el centro? creo que no
caja[Nx/2,Ny/2] = 1
if Nx % 2 == 0:
    caja[(Nx / 2) - 1 ,Ny / 2] = 1
if Ny % 2 == 0:
    caja[Nx / 2 ,(Ny / 2) - 1] = 1
'''

#######################################################

#construir letra
'''
dentro de caja de 5cmx7cm
construir letra M
grosor 1cm
'''
Llx = 5              #largo caja de letra eje x
Lly = 7              #largo caja de letra eje y
Nlx = (Llx / h) + 1  #numero de pasos en caja de letra a dar en eje x
Nly = (Lly / h) + 1  #numero de pasos en caja de ltera a dar en eje y

cajal = np.ones( (Nlx , Nly) ) #se construye caja de letra

borde_x_caja1 = (Lx / 2 - Llx) / h
borde_y_caja1 = (Ly / 2 - Lly) / h
borde_x_caja2 = (Lx / 2 + Llx) / h
borde_y_caja2 = (Ly / 2 + Lly) / h

caja[borde_x_caja1 : borde_x_caja2 , borde_y_caja1 : borde_y_caja2] = cajal

#######################################################

#construir condiciiones

#######################################################

#zona de pruebas
print borde_x_caja1
print borde_y_caja1
print borde_x_caja2
print borde_y_caja2
#caja[(Nx-1)/2,(Ny-1)/2] = 1

print np.transpose(caja)

#######################################################
