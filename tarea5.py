import matplotlib.pyplot as plt
import numpy as np
#Constantes Globales
h = 0.2
w = 1.3

#Definicion de Funciones
def LetraN(a, b):       #Obtiene indices, los que normaliza
    x = a * h - 5         #para que funcionen bien para la caja
    y = b * h - 7.5
    if x >= -2.5 and x < -1.5 and y >= -3.5 and y < 3.5:         #Retorna la densidad de carga
            return 0.05                                                           #dando la forma a la N
    elif x >= 1.5 and x < 2.5 and y >= -3.5 and y < 3.5:
            return 0.05
    elif x >= -1.5 and x < -0.5 and y >= 0.5 and y < 2.5:
            return 0.05
    elif x >= -0.5 and x < 0.5 and y >= -1 and y < 1:
            return 0.05
    elif x >= 0.5 and x < 1.5 and y >= -2.5 and y < -0.5:
            return 0.05
    else:
        return 0              #Retorna cero si está fuera de la letra


def SobreRelax(V):         #Modifica el valor del potencial actual V
    for i in range(1, 10):              #Segmento en X antes de la linea 
        for j in range(1, 75):                   #Y actua normal
            V[i][j] = ((1 - w) * V[i][j] + w / 4 * (V[i+1][j] +
                       V[i-1][j] + V[i][j+1] + V[i][j-1] +
                       h**2 * LetraN(i, j)))
    for i in range(41, 50):            #Segmento en X despues de la linea 
        for j in range(1, 75):                   #Y sigue actuando normal
            V[i][j] = ((1 - w) * V[i][j] + w / 4 * (V[i+1][j] +
                       V[i-1][j] + V[i][j+1] + V[i][j-1] +
                       h**2 * LetraN(i, j)))
    for i in range(10, 41):            #Segmento en X que contiene la linea
        for j in range(1, 9):                      #Hasta un poco antes de la linea
            V[i][j] = ((1 - w) * V[i][j] + w / 4 * (V[i+1][j] +
                       V[i-1][j] + V[i][j+1] + V[i][j-1] +
                       h**2 * LetraN(i, j)))
        for j in range(9, 10):                    #Borde inferior de la linea
            V[i][j] = ((1 - w) * V[i][j] + w / 3 * (V[i+1][j] +
                       V[i-1][j] + V[i][j-1] +
                       h**2 * LetraN(i, j) - h))
        for j in range(10, 11):                  #Sobre la linea para abajo
            V[i][j] = V[i][j+1] - h
        for j in range(11, 12):                  #Sobre la linea para arriba
            V[i][j] = V[i][j-1] + h
        for j in range(12, 13):                  #Borde Superior de la linea
            V[i][j] = ((1 - w) * V[i][j] + w / 3 * (V[i+1][j] +
                       V[i-1][j] + V[i][j-1] +
                       h**2 * LetraN(i, j) + h))
        for j in range(13, 75):                  #Desde arriba de la linea hasta el final
            V[i][j] = ((1 - w) * V[i][j] + w / 4 * (V[i+1][j] +
                       V[i-1][j] + V[i][j+1] + V[i][j-1] +
                       h**2 * LetraN(i, j)))
#No se toma en cuenta el 0 ni los indices 51 ni 76 porque el potencial es 0 por conexion a tierra

def Convergencia(V, NewV):         #Entrega respuesta de si Converge o no
    QuitaCero = (NewV != 0)                                  
    Dif = (V - NewV)[QuitaCero] / NewV[QuitaCero]  #Evalua la diferencia
    DifMax = np.max(np.fabs(Dif))                           #Obteniendo la máxima
    if DifMax > 1e-3:                                              #Compara con una tolerancia para decidir
        return True
    else:
        return False

Npuntos = []                                      #Se hace el arreglo para
for a in range(51):                              #dibujar la letra.
    Npuntos.append([])                        #Se arma una cuadrícula y 
    for b in range(76):                          #se rellena con los valores
        Npuntos[a].append(LetraN(a, b)) #de la funcion LetraN

Npuntos = np.arcsinh(np.transpose(Npuntos))  #Transpone para poder graficar
#Plots de la letra                                           #en la direccion correcta
fig = plt.figure()
plt.imshow(Npuntos, origin='bottom',
           interpolation='nearest', extent=[-5, 5, -7.5, 7.5])
plt.colorbar()
plt.xlabel('$X[cm]$')
plt.ylabel('$Y[cm]$')
plt.title('$Densidad$ $de$ $Carga$ $[C/cm^2]$')
plt.show()
fig.savefig('Densidad de Carga.png')
#Ajuste de variables para integrar
V = np.zeros((51, 76))
GuardaV = np.zeros((51, 76))
SobreRelax(V)
N = 0       #Variable auxiliar para iterar
while N < 3000 and Convergencia(GuardaV, V): #Evalua iteraciones y convergencia
    for a in range(len(GuardaV)):           #Este codigo es para
        for b in range(len(GuardaV[a])):   #guardar el V acutal para
            GuardaV[a][b] = V[a][b]          #poder compararlo con el proximo V
    SobreRelax(V)         #Aplica los cambios con el metodo
    N += 1
print ('Para w= '+str(w)+' converge con '+str(N)+' iteraciones.')    #Entrega numero de iteraciones.
#Guarda datos para el tercer gráfico, antes de que se traspongan
Yy = V[25]
Yx = np.linspace(-7.5, 7.5, 76)

V = np.arcsinh(np.transpose(V))     #Transpone para correcta orientacion 
#Plots potencial electrostarico
fig = plt.figure()
plt.imshow(V, origin='bottom',
           interpolation='nearest', extent=[-5, 5, -7.5, 7.5])
plt.colorbar()
plt.xlabel('$X[cm]$')
plt.ylabel('$Y[cm]$')
plt.title('$Potencial$ $Electrostático$ $[Volt]$ $w=$ $'+str(w)+'$')
plt.show()
fig.savefig('Potencial Electrostatico w'+str(w)+'.png')
#Plot perfil de potencial
fig = plt.figure()
plt.plot(Yx, Yy)
plt.xlim(-7.5, 7.5)
plt.ylim(-2, 0.5)
plt.xlabel('$Y[cm]$')
plt.ylabel('$[Volt]$')
plt.title('$Perfil$ $de$ $Potencial$')
plt.show()
fig.savefig('Perfil de Potencial.png')
