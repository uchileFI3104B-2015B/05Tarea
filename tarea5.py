from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

densidad=1/19.
h=0.2 #paso, en centímetros
L_x=10 #ancho de la grilla, está en centímetros
L_y=15 #alto de la grilla, está en centímetros
Steps_x=int((L_x/h)+1) #número de pasos en X
Steps_y=int((L_y/h)+1) #número de pasos en Y
omega=1.8
tolerance=1e-3

def rho(i, j, h):
    x=i*h-(L_x/2.) #los x e y están en centímetros, el origen está en el centro de la grilla
    y=j*h-(L_y/2.)
    if (x>=-2.5 and x<=2.5) and (y>=-3.5 and y<=-2.5): #palito de abajo de la E
        return densidad
    elif (x>=-2.5 and x<=2.5) and (y>=-0.5 and y<=0.5): #palito del medio de la E
        return densidad
    elif (x>=-2.5 and x<=2.5) and (y>=2.5 and y<=3.5): #palito de arriba de la E
        return densidad
    elif (x>=-2.5 and x<=-1.5) and (y>=-2.5 and y<=-0.5): #segmento entre palito de abajo y el del medio
        return densidad
    elif (x>=-2.5 and x<=-1.5) and (y>=0.5 and y<=2.5): #segmento entre palito del medio y el de arriba
        return densidad
    else:
        return 0

def una_iteracion(v,v_next,Steps_x,Steps_y,h,w=omega): #aquí hay que separar para 2 casos: la línea que es C.B. y el resto
    for i in range(1,Steps_x-1):
        for j in range(1,12): #abajo de la línea
            v_next[i,j]=((1-w)*v[i,j]+(w/4.)*(v[i+1,j]+v_next[i-1,j]+v[i,j+1]+v_next[i,j-1]+h**2*rho(i,j,h)))
        for j in range(14,Steps_y-1): #arriba de la línea
            v_next[i,j]=((1-w)*v[i,j]+(w/4.)*(v[i+1,j]+v_next[i-1,j]+v[i,j+1]+v_next[i,j-1]+h**2*rho(i,j,h)))
    for j in range(12,14):
        for i in range(1,11): #a la izquierda de la línea
            v_next[i,j]=((1-w)*v[i,j]+(w/4.)*(v[i+1,j]+v_next[i-1,j]+v[i,j+1]+v_next[i,j-1]+h**2*rho(i,j,h)))
        for i in range(41,Steps_x-1): #a la derecha de la línea
            v_next[i,j]=((1-w)*v[i,j]+(w/4.)*(v[i+1,j]+v_next[i-1,j]+v[i,j+1]+v_next[i,j-1]+h**2*rho(i,j,h)))
    for i in range(11,41):
        for j in range(12,13): #justo debajo de la línea, donde aplica la condición -1
            v_next[i,j]=((1-w)*v[i,j]+(w/3.)*(v[i+1,j]+v_next[i-1,j]+v_next[i,j-1]+h**2*rho(i,j,h)-h))
        for j in range(13,14): #justo sobre la línea, donde aplica la condición +1
            v_next[i,j]=((1-w)*v[i,j]+(w/3.)*(v[i+1,j]+v_next[i-1,j]+v_next[i,j-1]+h**2*rho(i,j,h)+h))

def no_ha_convergido(v,v_next,tol=tolerance):
    not_zero=(v_next!=0)
    diff_relativa=(v-v_next)[not_zero]/v_next[not_zero]
    max_diff=np.max(np.fabs(diff_relativa))
    if max_diff>tol:
        return True
    else:
        return False

V=np.zeros((Steps_x,Steps_y)) #genero grillas llenas con ceros, esto me da por garantizado que en el borde V=0
V_next=np.zeros((Steps_x,Steps_y))

una_iteracion(V,V_next,Steps_x,Steps_y,h,w=omega)
counter=1
while counter<2000 and no_ha_convergido(V,V_next,tol=tolerance):
    V=V_next.copy()
    una_iteracion(V,V_next,Steps_x,Steps_y,h,w=omega)
    counter+=1
print("counter={}".format(counter))
print(omega)
V_trans=V_next.transpose()

fig=plt.figure(1)
fig.clf()
ax=fig.add_subplot(111,projection='3d')
x=np.linspace(-1,1,Steps_x)
y=np.linspace(-1,1,Steps_y)
X,Y=np.meshgrid(x,y)
ax.plot_surface(X,Y,V_trans,rstride=1,cstride=1)
plt.savefig('plot_surface.png')
fig.show()

fig2=plt.figure(2)
fig2.clf()
ax2=fig2.add_subplot(111)
ax2.imshow(V_trans,origin='bottom',interpolation='nearest')
plt.savefig('plot_imshow.png')
fig2.show()
