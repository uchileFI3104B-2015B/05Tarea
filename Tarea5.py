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


def crea_caja(Lx, Ly, h):
    '''
    crea caja con zeros de tamanho Lx x Ly con cuadrillas de paso h
    '''
    Nx = (Lx / h) + 1  # numero de pasos a dar en eje x
    Ny = (Ly / h) + 1  # numero de pasos a dar en eje y
    caja = np.zeros((Nx, Ny))  # se construye caja

    return caja

#######################################################


def letra_M(caja, h, rho):
    '''
    construye letra M densidad de carga rho
    en caja de largo Lx x Ly y con paso h
    '''
    Llx = (len(caja[:, 0]) - 1) * h      # largo caja de letra eje x
    Lly = (len(caja[0, :]) - 1) * h      # largo caja de letra eje y
    Nlx = len(caja[:, 0])   # numero de pasos en caja de letra a dar en eje x
    Nly = len(caja[0, :])   # numero de pasos en caja de ltera a dar en eje y
    N_pasos_1cm = 1. / h    # numero de pasos para tener 1 cm

    cajal = crea_caja(Llx, Lly, h)

    cajal[0: 0 + N_pasos_1cm, :] = rho     # |iz

    cajal[Nlx - N_pasos_1cm: Nlx, :] = rho   # |der

    cajal[:, N_pasos_1cm: 2 * N_pasos_1cm] = rho   # -superior

    cajal[Nlx / 2 - N_pasos_1cm / 2: Nlx / 2 + N_pasos_1cm / 2 + 1,
          2 * N_pasos_1cm: 3 * N_pasos_1cm] = rho   # -centro inferior

    A = cajal[Nlx / 2 - N_pasos_1cm / 2: Nlx / 2 + N_pasos_1cm / 2
              + 1, N_pasos_1cm: 2 * N_pasos_1cm]
    B = caja[Nlx / 2 - N_pasos_1cm / 2: Nlx / 2 + N_pasos_1cm / 2
             + 1, N_pasos_1cm: 2 * N_pasos_1cm]
    A = B  # -centro superior

    return cajal

#######################################################


def asignar_caja_letra(caja, cajal, h):
    '''
    asigna la caja de letra a la caja principal
    caja principal caja Lx x Ly
    caja de letra cajal Llx x Lly
    paso h
    '''
    Nx = len(caja[:, 0])     # numero de pasos a dar en eje x
    Ny = len(caja[0, :])     # numero de pasos a dar en eje y
    Nlx = len(cajal[:, 0])   # numero de pasos en caja de letra a dar en eje x
    Nly = len(cajal[0, :])   # numero de pasos en caja de ltera a dar en eje y

    bordex_caja = round((Nx / 2) - (Nlx / 2))
    bordey_caja = round((Ny / 2) - (Nly / 2))

    caja[bordex_caja: bordex_caja + Nlx,
         bordey_caja: bordey_caja + Nly] = cajal

    return caja

#######################################################


def una_iteracion_completa(V, V_next, Rho, h, w=1.2):
    '''
    Hace una iteracion completa sobre toda la caja
    se hace la iteracion por partes, desde la parte superior a la inferior
    '''
    Nx = len(V[:, 0])
    Ny = len(V[0, :])
    a = int(round(2 / h))
    b = int(round(8 / h)) + 1
    linea = int(round(13 / h))  # linea en 13/h

    '''primera parte de la caja'''
    for i in range(1, Nx - 1):
        for j in range(1, linea - 1):
            V_next[i, j] = ((1 - w) * V[i, j] +
                            w / 4 * (V[i+1, j] + V_next[i-1, j] +
                                     (V[i, j + 1] + V_next[i, j - 1] +
                                      h**2 * Rho[i, j])))

    '''1 antes de la linea g=1'''
    for i in range(a, b):
        V_next[i, linea - 1] = ((1 - w) * V[i, linea - 1]
                                 + w / 3 * (V[i+1, linea - 1]
                                 + V_next[i-1, linea - 1]
                                 + V_next[i, linea - 2]
                                 - h + h**2 * Rho[i, j]))

    '''integracion sobre la linea'''
    for i in range(a, b):
        V_next[i, linea] = V[i, linea - 1] + h  # condicion g=1

    '''1 despues de la linea g=-1'''
    for i in range(a, b):
        V_next[i, linea + 1] = ((1 - w) * V[i, linea + 1]
                                 + w / 3 * (V[i+1, linea + 1]
                                 + V_next[i-1, linea + 1]
                                 + V_next[i, linea + 2]
                                 + h + h**2 * Rho[i, j]))

    '''parte izquierda de la linea'''
    for i in range(1, a):
        for j in range(linea - 1, linea + 2):
            V_next[i, j] = ((1 - w) * V[i, j] +
                            w / 4 * (V[i+1, j] + V_next[i-1, j] +
                                     (V[i, j + 1] + V_next[i, j - 1] +
                                      h**2 * Rho[i, j])))

    '''parte derecha de la linea'''
    for i in range(b, Nx - 1):
        for j in range(linea - 1, linea + 2):
            V_next[i, j] = ((1 - w) * V[i, j] +
                            w / 4 * (V[i+1, j] + V_next[i-1, j] +
                                     (V[i, j + 1] + V_next[i, j - 1] +
                                      h**2 * Rho[i, j])))

    '''ultima parte de la caja'''
    for i in range(1, Nx - 1):
        for j in range(linea + 2, Ny - 1):
            V_next[i, j] = ((1 - w) * V[i, j] +
                            w / 4 * (V[i+1, j] + V_next[i-1, j] +
                                     (V[i, j + 1] + V_next[i, j - 1] +
                                      h**2 * Rho[i, j])))

#######################################################


def no_ha_convergido(V, V_next, tolerancia=1e-5):
    '''
    Compara el potencial actual con el del paso anterior y determina si
    ha convergido o no a partir de nuestra tolerancia
    '''
    not_zero = (V_next != 0)
    diff_relativa = (V - V_next)[not_zero] / V_next[not_zero]
    max_diff = np.max(np.fabs(diff_relativa))
    if max_diff > tolerancia:
        return True
    else:
        return False

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

Lx = 10.           # [cm] largo de la caja en eje x
Ly = 15.           # [cm] largo de la caja en eje y
h = 0.25           # [cm] tamanho del paso
w = 1.6            # w parametro del metodo de sobrerelajacion

caja = crea_caja(Lx, Ly, h)  # se construye caja

#######################################################

#construir letra
'''
dentro de caja de 5cmx7cm
construir letra M
grosor 1cm
'''
Llx = 5.       # largo caja de letra eje x
Lly = 7.       # largo caja de letra eje y

rho = (1. / 17.) * h**2      # densidad de carga, son 17cm2 de letra

cajal = crea_caja(Llx, Lly, h)    # se construye caja de letra

cajal = letra_M(cajal, h, rho)   # se construye letra M en la caja de letra

'''
asignacion de la letra a la caja principal
'''

caja = asignar_caja_letra(caja, cajal, h)  # se asigna letra a caja principal

#######################################################

# aplicar metodo de sobrerelajacion
'''
rho solo existe en la letra, en los demas puntos es cero
'''
Lx = 10.            # [cm] largo de la caja en eje x
Ly = 15.            # [cm] largo de la caja en eje y
h = 0.25            # [cm] tamanho del paso
w = 1.4             # w parametro del metodo de sobrerelajacion
tolerancia = 1e-7   # Diferencia esperada para considerar convergencia
Niteracion = 10000  # Numero de iteracion maxima

Rho = crea_caja(Lx, Ly, h)
Rho = asignar_caja_letra(Rho, cajal, h)  # G_ij

V = crea_caja(Lx, Ly, h)
V_next = crea_caja(Lx, Ly, h)

una_iteracion_completa(V, V_next, Rho, h, w)
counter = 1

while counter < Niteracion and no_ha_convergido(V, V_next, tolerancia):
    V = V_next.copy()
    una_iteracion_completa(V, V_next, Rho, h, w)
    counter += 1

print("w = {}".format(w))
print("Numero de iteracion maxima = {}".format(Niteracion))
print("counter = {}".format(counter))

sum_rho = sum(sum(Rho))
print 'densidad de carga = ', rho, '[C / cm2]'
print 'carga total = ', sum_rho, '[C]'

#######################################################
#graficos

plt.imshow(np.arcsinh(np.transpose(V_next)), interpolation='nearest',
           extent=[-5, 5, -7.5, 7.5])

plt.title('Potencial electroestatico')

# plt.imshow(np.transpose(Rho) , interpolation='nearest',
#            extent=[-5, 5, -7.5, 7.5])

# plt.title('Densidad de carga')

plt.xlabel('eje x [cm]')
plt.ylabel('eje y [cm]')
plt.colorbar()
plt.show()

#######################################################
