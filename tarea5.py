from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

densidad=1/19.
h=0.1 #paso, en centímetros
L_x=10 #ancho de la grilla, está en centímetros
L_y=15 #alto de la grilla, está en centímetros
Steps_x=L_x/h
Steps_y=L_y/h

def show(phi):
    print(phi[::-1, :])

def rho(i, j, h):
    x=i*h-(L_x/2.) #los x e y están en centímetros, el origen está en el centro de la grilla
    y=j*h-(L_y/2.)
    if (x>=2.5 and x<=7.5) and (y>=4 and y<=5): #palito de abajo de la E
        return densidad
    elif (x>=2.5 and x<=7.5) and (y>=7 and y<=8): #palito del medio de la E
        return densidad
    elif (x>=2.5 and x<=7.5) and (y>=10 and y<=11): #palito de arriba de la E
        return densidad
    elif (x>=2.5 and x<=3.5) and (y>=5 and y<=7): #segmento entre palito de abajo y el de al medio
        return densidad
    elif (x>=2.5 and x<=3.5) and (y>=9 and y<=10): #segmento entre palito del medio y el de arriba
        return densidad
    else:
        return 0

def una_iteracion(phi,phi_next,Steps_x,Steps_y,h,w=1.):
    for i in range(1,Steps_x-1):
        for j in range(1,Steps_y-1):
            phi_next[i,j]=((1-w)*phi[i,j]+(w/4)*(phi[i+1,j]+phi_next[i-1,j]+phi[i,j+1]+phi_next[i,j-1]+h**2*rho(i,j,h)))

V=np.zeros((Steps_x,Steps_y))
V_next=np.zeros((Steps_x,Steps_y))
