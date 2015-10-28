import matplotlib.pyplot as plt
import numpy as np

h=0.2

def LetraN(a, b):
    x = a * h - 5
    y = b * h - 7.5
    if x >= -2.5 and x < -1.5 and y >= -3.5  and y < 3.5:
            return 0.05
    elif x >= 1.5 and x < 2.5 and y >= -3.5 and y < 3.5:
            return 0.05
    elif x >= -1.5 and x < -0.5 and y >= 0.5 and y < 2.5:
            return 0.05
    elif x >= -0.5 and x < 0.5 and y >= -1 and y < 1:
            return 0.05
    elif x >= 0.5 and x < 1.5 and y >= -2.5 and y < -0.5:
            return 0.05
    else:
        return 0

def SobreRelax(V, w=1.3):
    for i in range(1, 10):
        for j in range(1, 75):
            V[i][j] = ((1 - w) * V[i][j] +
                            w / 4 * (V[i+1][j] + V[i-1][j] +
                                     V[i][j+1] + V[i][j-1] +
                                     h**2 * LetraN(i,j)))
    for i in range(41, 50):
        for j in range(1, 75):
            V[i][j] = ((1 - w) * V[i][j] +
                            w / 4 * (V[i+1][j] + V[i-1][j] +
                                     V[i][j+1] + V[i][j-1] +
                                     h**2 * LetraN(i,j)))
    for i in range(10, 41):
        for j in range(1, 9):
            V[i][j] = ((1 - w) * V[i][j] +
                            w / 4 * (V[i+1][j] + V[i-1][j] +
                                     V[i][j+1] + V[i][j-1] +
                                     h**2 * LetraN(i,j)))
        for j in range(9, 10):
            V[i][j] = ((1 - w) * V[i][j] +
                            w / 3 * (V[i+1][j] + V[i-1][j] +
                                     V[i][j-1] + h**2* LetraN(i,j)
                                     -h))
        for j in range(10, 11):
            V[i][j] = V[i][j+1] - h
        for j in range(11, 12):
            V[i][j] = ((1 - w) * V[i][j] +
                            w / 3 * (V[i+1][j] + V[i-1][j] +
                                     V[i][j-1] + h**2* LetraN(i,j)
                                     +h))
        for j in range(12, 75):
            V[i][j] = ((1 - w) * V[i][j] +
                            w / 4 * (V[i+1][j] + V[i-1][j] +
                                     V[i][j+1] + V[i][j-1] +
                                     h**2 * LetraN(i,j)))

Npuntos = []
for a in range(51):
    Npuntos.append([])
    for b in range(76):
        Npuntos[a].append(LetraN(a,b))
        
Npuntos=np.arcsinh(np.transpose(Npuntos))
plt.imshow(Npuntos, origin='bottom', interpolation='nearest', extent=[-5, 5, -7.5, 7.5])
plt.colorbar()
plt.show()

V = np.zeros((51, 76))
GuardaV = V
SobreRelax(V) 
N = 0
while N < 400:
    GuardaV = V
    SobreRelax(V)   
    N += 1
print (N)

V=np.arcsinh(np.transpose(V))
plt.imshow(V, origin='bottom', interpolation='nearest', extent=[-5, 5, -7.5, 7.5])
plt.colorbar()
plt.show()
