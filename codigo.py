import numpy as np


Lx=10
Ly=15
h=0.2
N_pasos_x = Lx / h + 1
N_pasos_y = Ly / h + 1

phi=np.zeros( ( N_pasos_x , N_pasos_y ) )

def rho(i, j, h):
    x = i * h - 5
    y = j * h - 7.5
    rho_letra = 1 / 23
    rho_blanco = 0

    if x >= -2.5 and x <= -1.5 and y >= -3.5 and y <= 3.5:
        return rho_letra
    if x >= 1.5 and x <= 2.5 and y >= -3.5 and y <= 3.5:
        return rho_letra
    if y <= 3.5 and x >= 2.5 and x > -1.5 and x < 1.5:
        return rho_letra
    if y <= 0.5 and y >= -0.5 and x > -1.5 and x < 1.5:
        return rho_letra
    if y <= -2.5 and y >= -3.5 and x > -1.5 and x < 1.5:
        return rho_letra
    else:
        return rho_blanco

print phi
