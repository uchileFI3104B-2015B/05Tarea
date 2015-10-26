from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

densidad=1/19.
h=0.1 #paso, en centímetros
L_x=10 #ancho de la grilla, está en centímetros
L_y=15 #alto de la grilla, está en centímetros
Steps_x=int(L_x/h)+1
Steps_y=int(L_y/h)+1

def show(phi):
    print(phi[::-1, :])

def rho(i, j, h):
    x=i*h-(L_x/2.) #los x e y están en centímetros, el origen está en el centro de la grilla
    y=j*h-(L_y/2.)
    if (x>=-2.5 and x<=2.5) and (y>=-3.5 and y<=-2.5): #palito de abajo de la E
        return densidad
    elif (x>=-2.5 and x<=2.5) and (y>=-0.5 and y<=0.5): #palito del medio de la E
        return densidad
    elif (x>=-2.5 and x<=2.5) and (y>=2.5 and y<=3.5): #palito de arriba de la E
        return densidad
    elif (x>=-2.5 and x<=-1.5) and (y>=-2.5 and y<=-0.5): #segmento entre palito de abajo y el de al medio
        return densidad
    elif (x>=-2.5 and x<=-1.5) and (y>=0.5 and y<=2.5): #segmento entre palito del medio y el de arriba
        return densidad
    else:
        return 0

def una_iteracion(v,v_next,Steps_x,Steps_y,h,w=1.): #aquí hay que separar para 3 casos: borde, línea y el resto
    for i in range(1,Steps_x-1):
        for j in range(1,12): #abajo de la línea
            phi_next[i,j]=((1-w)*phi[i,j]+(w/4)*(phi[i+1,j]+phi_next[i-1,j]+phi[i,j+1]+phi_next[i,j-1]+h**2*rho(i,j,h)))
        for j in range(14,Steps_y-1)]: #arriba de la línea
            phi_next[i,j]=((1-w)*phi[i,j]+(w/4)*(phi[i+1,j]+phi_next[i-1,j]+phi[i,j+1]+phi_next[i,j-1]+h**2*rho(i,j,h)))
    for j in range(12,14):
        for i in range(1,10): #a la izquierda de la línea
            phi_next[i,j]=((1-w)*phi[i,j]+(w/4)*(phi[i+1,j]+phi_next[i-1,j]+phi[i,j+1]+phi_next[i,j-1]+h**2*rho(i,j,h)))
        for i in range(41,Steps_y-1): #a la derecha de la línea
            phi_next[i,j]=((1-w)*phi[i,j]+(w/4)*(phi[i+1,j]+phi_next[i-1,j]+phi[i,j+1]+phi_next[i,j-1]+h**2*rho(i,j,h)))
    for i in range(11,41):
        for j in range(12,13):
            phi_next
V=np.zeros((Steps_x,Steps_y))
V_next=np.zeros((Steps_x,Steps_y))
