from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def ro (i,j,ly,lx,h):
    x= i*h - lx/2 #me paro en el centro
    y= j*h -ly/2
    dx= 2.5 # vamos al borde
    dy= 3.5
    a=1 #ancho del dibujito
    p= 1/15 # densidad por cuadradito
    tot=0
    if x >= -dx and x<= dx+a:
        if y >= -dy and y <= dy:
            tot= p
    if x >= a-dx and x<= dx:
        if y >= -dy and y <= -dy +a:
            tot= p
    if x >= a-dx and x<= dx:
        if y >= dy-a and y <= dy:
            tot= p
    return tot

def una_iteracion_cercaborde(phi, phi_next, N_pasos, h, w=1.):
    for i in range(1, N_pasos-1):
        for j in range(1, N_pasos-1):
            phi_next[i, j] = ((1 - w) * phi[i, j] +
                              w / 3 * (phi[i+1, j] + phi_next[i-1, j] +
                                       phi[i, j-1] -
                                       h**2 * ro(i, j, h)+ h*g(j)))

def una_iteracion_enelborde(phi, phi_next, N_pasos, h, w=1.):
    for i in range(1, N_pasos-1):
        for j in range(1, N_pasos-1):
            phi_next[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_next[i-1, j] +
                                       phi[i, j+1] + phi_next[i, j-1] ))


def no_ha_convergido(phi, phi_next, tolerancia=1e-5):
    not_zero = (phi_next != 0)
    diff_relativa = (phi - phi_next)[not_zero] / phi_next[not_zero]
    max_diff = np.max(np.fabs(diff_relativa))
    if max_diff > tolerancia:
        return True
    else:
        return False
