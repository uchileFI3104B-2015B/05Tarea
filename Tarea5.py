#######################################################
#######################################################
#######################################################
'''
Metodos Numericos para la Ciencia e Ingenieria
FI3104-1
Tarea 5
Maximiliano Dirk Vega Aguilera
18.451.231-9
'''
#######################################################
#######################################################
#######################################################

import numpy as np
import matplotlib.pyplot as plt

#######################################################
#######################################################
#######################################################
#funciones

def crea_caja(Lx,Ly,h):
    '''
    crea caja con zeros de tamanho Lx x Ly con cuadrillas de paso h
    '''
    Nx = (Lx / h) + 1  #numero de pasos a dar en eje x
    Ny = (Ly / h) + 1  #numero de pasos a dar en eje y
    caja = np.zeros( (Nx , Ny) )  #se construye caja

    return caja

#######################################################

def letra_M(caja, h, rho):
    '''
    construye letra M densidad de carga rho
    en caja de largo Lx x Ly y con paso h
    '''
    Llx = (len(caja[:, 0]) - 1 ) * h              #largo caja de letra eje x
    Lly = (len(caja[0, :]) - 1 ) * h              #largo caja de letra eje y
    Nlx = len(caja[:, 0])  #numero de pasos en caja de letra a dar en eje x
    Nly = len(caja[0, :])   #numero de pasos en caja de ltera a dar en eje y
    N_pasos_1cm = 1. / h  #numero de pasos para tener 1 cm

    cajal = crea_caja(Llx, Lly, h)

    cajal[0 : 0 + N_pasos_1cm , : ] = rho    # |iz
    cajal[Nlx - N_pasos_1cm : Nlx , : ] = rho #|der

    cajal[ : , N_pasos_1cm : 2 * N_pasos_1cm] = rho #-superior

    cajal[Nlx / 2 - N_pasos_1cm / 2 : Nlx / 2 + N_pasos_1cm / 2 + 1 ,
    2 * N_pasos_1cm : 3 * N_pasos_1cm] = rho   #-centro inferior

    cajal[Nlx / 2 - N_pasos_1cm / 2 : Nlx / 2 + N_pasos_1cm / 2 + 1 ,
    N_pasos_1cm : 2 * N_pasos_1cm ] = caja[Nlx / 2 - N_pasos_1cm / 2 :
     Nlx / 2 + N_pasos_1cm / 2 + 1 , N_pasos_1cm : 2 * N_pasos_1cm ] #-centrosup

    return cajal

#######################################################

def asignar_letra(caja, Lx , Ly, cajal, Llx, Lly, h):
    '''
    asigna la letra a la caja principal
    caja principal caja Lx x Ly
    caja de letra cajal Llx x Lly
    paso h
    '''
    Nx = len(caja[:, 0])   #numero de pasos a dar en eje x
    Ny = len(caja[0, :])  #numero de pasos a dar en eje y
    Nlx = len(cajal[:, 0])    #numero de pasos en caja de letra a dar en eje x
    Nly = len(cajal[0, :])   #numero de pasos en caja de ltera a dar en eje y

    bordex_caja = round((Nx / 2 ) - (Nlx / 2 ))
    bordey_caja = round((Ny / 2 ) - (Nly / 2 ))

    ly = int(round(Nlx))
    lx = int(round(Nly))

    try:
        lx = int(round(Nly))
        try:
            ly = int(round(Nlx))
            for i in range(ly):
                for j in range(lx):
                    if cajal[i][j] != 0:
                        if cajal[i][j] != 0:
                            caja[bordex_caja : bordex_caja + Nlx ,
                            bordey_caja : bordey_caja + Nly][i][j] = cajal[i][j]
        except:
            ly = int(round(Nlx)) -1
            for i in range(ly):
                for j in range(lx):
                    if cajal[i][j] != 0:
                        if cajal[i][j] != 0:
                            caja[bordex_caja : bordex_caja + Nlx ,
                            bordey_caja : bordey_caja + Nly][i][j] = cajal[i][j]
    except:
        lx = int(round(Nly)) - 1
        try:
            ly = int(round(Nlx))
            for i in range(ly):
                for j in range(lx):
                    if cajal[i][j] != 0:
                        if cajal[i][j] != 0:
                            caja[bordex_caja : bordex_caja + Nlx ,
                            bordey_caja : bordey_caja + Nly][i][j] = cajal[i][j]
        except:
            ly = int(round(Nlx)) -1
            for i in range(ly):
                for j in range(lx):
                    if cajal[i][j] != 0:
                        if cajal[i][j] != 0:
                            caja[bordex_caja : bordex_caja + Nlx ,
                            bordey_caja : bordey_caja + Nly][i][j] = cajal[i][j]

    return caja

#######################################################

def asignar_caja_letra(caja, cajal, h):
    '''
    asigna la caja de letra a la caja principal
    caja principal caja Lx x Ly
    caja de letra cajal Llx x Lly
    paso h
    '''
    Nx = len(caja[:, 0])   #numero de pasos a dar en eje x
    Ny = len(caja[0, :])  #numero de pasos a dar en eje y
    Nlx = len(cajal[:, 0])    #numero de pasos en caja de letra a dar en eje x
    Nly = len(cajal[0, :])   #numero de pasos en caja de ltera a dar en eje y

    bordex_caja = round((Nx / 2 ) - (Nlx / 2 ))
    bordey_caja = round((Ny / 2 ) - (Nly / 2 ))

    caja[bordex_caja : bordex_caja + Nlx ,
    bordey_caja : bordey_caja + Nly] = cajal

    return caja

#######################################################

def una_iteracion_normal(V, V_next, Rho, h, w=1.2):
    Nx = len(V[:,0])
    Ny = len(V[0,:])
    for i in range(1, Nx - 1):
        for j in range(1, Ny - 1):
            V_next[i, j] = ((1 - w) * V[i, j] +
                              w / 4 * (V[i+1, j] + V_next[i-1, j] +
                                       V[i, j + 1] + V_next[i, j - 1] +
                                       h**2 * Rho[i,j]))   # + porque es -Rho

#######################################################

def una_iteracion_linea(V, V_next, Rho, h, w=1.2):
    Nx = len(V[:,0])
    Ny = len(V[0,:])
    cajalinea = crea_caja(Lx,Ly,h)
    cajalinea[2 / h : 8 / h + 1 , 13 / h - 1 : 13 / h +1] = 3  #linea en 13 / h
    Nlx = len(cajalinea[ 2 / h : 8 / h +1 , 13 / h])
    a = round(2 / h)
    b = round(8 / h) + 1
    for i in range(int(a), int(b)):
        V_next[i, 13 / h] = V[i, 13 / h - 1] + h  # condicion g=1
        V_next[i, 13 / h + 1] = V[i, 13 / h] - h  # condicion g=-1

#######################################################

def una_iteracion_completa(V, V_next, Rho, h, w=1.2):
    Nx = len(V[:,0])
    Ny = len(V[0,:])
    cajalinea = crea_caja(Lx,Ly,h)
    cajalinea[2 / h : 8 / h + 1 , 13 / h - 1 : 13 / h +1] = 3  #linea en 13 / h
    a = int(round(2 / h))
    b = int(round(8 / h)) + 1
    linea = int(round(13 / h))

    for i in range(1, Nx - 1): #primera parte de la caja
        for j in range(1, linea - 2):
            V_next[i, j] = ((1 - w) * V[i, j] +
                              w / 4 * (V[i+1, j] + V_next[i-1, j] +
                                       V[i, j + 1] + V_next[i, j - 1] +
                                       h**2 * Rho[i,j]))

    for i in range(int(a), int(b)): #1 antes de la linea g=1
        V_next[i, 13 / h - 1] = ((1 - w) * V[i, 13 / h - 1]
                                 + w / 3 * (V[i+1, 13 / h - 1]
                                 + V_next[i-1, 13 / h - 1]
                                 + V_next[i, 13 / h - 2]
                                 + h + h**2 * Rho[i,j]))


    for i in range(int(a), int(b)): #integracion sobre la linea
        V_next[i, 13 / h] = V[i, 13 / h - 1] + h  # condicion g=1
        V_next[i, 13 / h + 1] = V[i, 13 / h] - h  # condicion g=-1


    for i in range(int(a), int(b)): #1 despues de la linea g=-1
        V_next[i, 13 / h + 2] = ((1 - w) * V[i, 13 / h + 2]
                                 + w / 3 * (V[i+1, 13 / h + 2]
                                 + V_next[i-1, 13 / h + 2]
                                 + V_next[i, 13 / h + 1]
                                 - h + h**2 * Rho[i,j]))


    for i in range(1, a - 1): #parte izquierda de la caja
        for j in range(linea - 2 , linea + 2):
            V_next[i, j] = ((1 - w) * V[i, j] +
                              w / 4 * (V[i+1, j] + V_next[i-1, j] +
                                       V[i, j + 1] + V_next[i, j - 1] +
                                       h**2 * Rho[i,j]))

    for i in range(b + 1, Nx - 1): #parte derecha de la caja
        for j in range(linea - 2 , linea + 2):
            V_next[i, j] = ((1 - w) * V[i, j] +
                              w / 4 * (V[i+1, j] + V_next[i-1, j] +
                                       V[i, j + 1] + V_next[i, j - 1] +
                                       h**2 * Rho[i,j]))

    for i in range(1, Nx - 1): #ultima parte de la caja
        for j in range(linea + 2, Ny -1):
            V_next[i, j] = ((1 - w) * V[i, j] +
                              w / 4 * (V[i+1, j] + V_next[i-1, j] +
                                       V[i, j + 1] + V_next[i, j - 1] +
                                       h**2 * Rho[i,j]))



#######################################################
#######################################################
#######################################################

#construir caja
'''
caja de 10cmx15cm
centro de caja = (0,0)
cambio de coordenadas
x' = x - Nx/2
y' = y - Ny/2
esquina de caja = (0,0)
'''
Lx = 10.           #[cm] largo de la caja en eje x
Ly = 15.           #[cm] largo de la caja en eje y
h = 0.25           #[cm] tamanho del paso (recomiendo 0.25 (?))
w = 1.             # w parametro del metodo de sobrerelajacion

caja = crea_caja(Lx, Ly, h)  #se construye caja

#######################################################

#construir letra
'''
dentro de caja de 5cmx7cm
construir letra M
grosor 1cm
'''
Llx = 5.       #largo caja de letra eje x
Lly = 7.       #largo caja de letra eje y

rho = (1. /  17.) * h**2      #densidad de carga, son 17cm2 de letra
rho=1
cajal = crea_caja(Llx, Lly, h)    #se construye caja de letra
cajal = letra_M(cajal, h, rho) #se construye letra M en la caja de letra

'''
asignacion de la letra a la caja principal
'''

caja = asignar_caja_letra(caja, cajal, h) #se asigna letra a caja principal

#######################################################

#construir condiciiones
'''
voltaje en los borde = 0 ... construir en la iteracion
rho esta en la definicion de la letra
'''
#crear linea
'''
la linea se encuetra en el cm 13 en y, y entre el cm 2 y 8 en x
'''


cajalinea = crea_caja(Lx,Ly,h)
cajalinea[2 / h : 8 / h + 1 , 13 / h - 1 : 13 / h +1] = 3  #linea en 13 / h



#######################################################

#aplicar metodo de sobrerelajacion
'''
rho solo existe en la letra, en los demas puntos es cero
'''
Rho = crea_caja(Lx, Ly, h)
Rho = asignar_caja_letra(Rho, cajal, h) #G_ij

V = crea_caja(Lx, Ly, h)
V_next = crea_caja(Lx, Ly, h)






#######################################################


#zona de pruebas
#print bordex_caja
#print bordey_caja

#caja[(Nx-1)/2,(Ny-1)/2] = 1

#print sum(sum(cajal)) #carga total en letra
#print np.transpose(caja)
#print np.transpose(cajal)
#print np.transpose(Rho)
#una_iteracion_linea(V, V_next, Rho, h, w=1.2)
#una_iteracion_normal(V, V_next, Rho, h, w=1.2)
#una_iteracion_linea(V, V_next, Rho, h, w=1.2)
una_iteracion_completa(V, V_next, Rho, h, w=1.2)
counter = 1
while counter < 1500 :
    V = V_next.copy()
    una_iteracion_completa(V, V_next, Rho, h, w=1.2)
    counter += 1


plt.imshow(np.transpose(V_next) , interpolation = 'nearest')
#plt.imshow(np.arcsinh(np.transpose(V_next)) , interpolation = 'nearest')
plt.show()

#######################################################
