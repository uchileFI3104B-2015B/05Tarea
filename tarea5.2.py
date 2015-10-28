from math import *
from scipy import integrate as int
from scipy import optimize
from scipy.integrate import ode
import pyfits #modulo para leer archivos fits
import matplotlib.pyplot as p #modulo para graficar
import numpy as n #este modulo es para trabajar con matrices como en matlab
import matplotlib as mp
from mpl_toolkits.mplot3d import Axes3D

from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis, title, show
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

h=0.1  #paso

g=n.zeros((151,101))  #funcion densidad

for i in range(11):   #se define la funcion densidad con la letra B
    for j in range(71):
        g[j+40,i+25]=-10.0/23

for i in range(11):
    for j in range(71):
        g[j+40,i+65]=-10.0/23

for j in range(11):
    for i in range(29):
        g[j+40,i+36]=-10.0/23

for j in range(11):
    for i in range(29):
        g[j+70,i+36]=-10.0/23

for j in range(11):
    for i in range(29):
        g[j+100,i+36]=-10.0/23

x=n.linspace(-5.0,5.0,101)
y=n.linspace(-7.5,7.5,151)

X,Y=meshgrid(x,y)   #grilla de (x,y)

w=1.2  #factor de relajacion

V=n.zeros((len(y),len(x)))
U=n.zeros((len(y),len(x)))

r=100   #tolerancia
contador=0  #contador de convergencia




while r>0.00001:  #tolerancia maxima 0.0001

    #se aplica sobrerrelajacion sucesiva por zonas, de modo
    #de respetar las condiciones de borde
    
    for i in range(len(y)-2):   #zona -5 < x <-3 , para todo y
        for j in range(19):
            a=V[i+1,j+1]
            U[i+1,j+1]=a+w/4*(V[i+2,j+1]+U[i,j+1]+V[i+1,j+2]+U[i+1,j]-4.0*a -h**2*g[i+1,j+1])
            
    for i in range(18):   #zona -3< x <3, para y en [-7.5,-5.5]
        for j in range(61):
            a=V[i+1,j+20]
            U[i+1,j+20]=a+w/4*(V[i+2,j+20]+U[i,j+20]+V[i+1,j+21]+U[i+1,j+19]-4.0*a -h**2*g[i+1,j+20])




    for j in range(61):  #linea inferior a la condicion de neumann
        a=V[19,j+20]
        U[19,j+20]=a+w/4*(a+h+U[18,j+20]+V[19,j+21]+U[19,j+19]-4.0*a -h**2*g[19,j+20])
    

       

            

    for i in range(128):   #zona -3 < x < 3, para y en [-5.5, 7.5]
        for j in range(61):
            a=V[149-i,j+20]
            U[149-i,j+20]=a+w/4*(U[150-i,j+20]+V[148-i,j+20]+V[149-i,j+21]+U[149-i,j+19]-4.0*a -h**2*g[149-i,j+20])

    for j in range(61):   #linea superior a la condicion de neumann
        a=V[21,j+20]
        U[21,j+20]=a+w/4*(a-h+U[22,j+20]+V[21,j+21]+U[21,j+19]-4.0*a -h**2*g[21,j+20])

    for i in range(len(y)-2):   #zona 3 < x <5, para todo y
        for j in range(19):
            a=V[i+1,j+81]
            U[i+1,j+81]=a+w/4*(V[i+2,j+81]+U[i,j+81]+V[i+1,j+82]+U[i+1,j+80]-4.0*a -h**2*g[i+1,j+81])

    
    r=n.max(abs(U-V))   #diferencia entre U y V
    V=U.copy()
    contador=contador+1   #contador de convergencia


for j in range(61):    #se llena la línea de la condicion de neumann
    V[20,j+20]=V[19,j+20]+h



def graficaIntensidad(Z):

    'grafica curvas de nivel'

    #Se dibuja la funcion

    im = imshow(Z,cmap=cm.RdBu)

    

    #Se agrega el contorno de lineas con sus etiquetas

    cset = contour(Z,n.arange(-2.0,2.0,0.1),linewidths=2,cmap=cm.Set2)

    clabel(cset,inline=True,fmt='%1.1f',fontsize=10)

    

    #Se agrega la barra de colores a la derecha

    colorbar(im)



    show()

def grafica3D(X,Y,Z):

    'grafica funciones de 2 variables'

    fig = p.figure()

    fig.clf()

    ax = fig.add_subplot(111,projection='3d')

    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap=cm.RdBu,linewidth=0.15)

            

    fig.colorbar(surf, shrink=0.5, aspect=5)

    p.show()

grafica3D(X,Y,V)
graficaIntensidad(V)
p.plot(y,V[:,50])
p.xlabel('y [cm]')
p.ylabel('V')
p.show()

p.plot(y,V[:,18])
p.xlabel('y [cm]')
p.ylabel('V')
p.show()
print contador
