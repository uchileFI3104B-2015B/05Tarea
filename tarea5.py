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

def SobreRelax(V, w=1.4):
    for i in range(1, 50):
        for j in range(1, 10):
            V[i][j] = ((1 - w) * V[i][j] +
                            w / 4 * (V[i+1][j] + V[i-1][j] +
                                     V[i][j+1] + V[i][j-1] +
                                     h**2 * LetraN(i,j)))
        for j in range(11, 75):
            V[i][j] = ((1 - w) * V[i][j] +
                            w / 4 * (V[i+1][j] + V[i-1][j] +
                                     V[i][j+1] + V[i][j-1] +
                                     h**2 * LetraN(i,j)))
    for j in range(9, 12):
        for i in range(1, 10):
            V[i][j] = ((1 - w) * V[i][j] +
                            w / 4 * (V[i+1][j] + V[i-1][j] +
                                     V[i][j+1] + V[i][j-1] +
                                     h**2 * LetraN(i,j)))
        for i in range(41, 50):
            V[i][j] = ((1 - w) * V[i][j] +
                            w / 4 * (V[i+1][j] + V[i-1][j] +
                                     V[i][j+1] + V[i][j-1] +
                                     h**2 * LetraN(i,j)))
    for i in range(10, 41):
        for j in range(9, 10):
            V[i][j] = ((1 - w) * V[i][j] +
                            w / 3 * (V[i+1][j] + V[i-1][j] +
                                     V[i][j-1] + h**2* LetraN(i,j) +
                                     -h))
        for j in range(10, 11):
            V[i][j] = ((1 - w) * V[i][j] +
                            w / 3 * (V[i+1][j] + V[i-1][j] +
                                     V[i][j-1] + h**2 * LetraN(i,j) +
                                     h))

Npuntos = []
for a in range(51):
    Npuntos.append([])
    for b in range(76):
        Npuntos[a].append(LetraN(a,b))
        
Npuntos=np.arcsinh(np.transpose(Npuntos))
plt.imshow(Npuntos, origin='bottom', interpolation='nearest', extent=[-5, 5, -7.5, 7.5])
plt.show()

V = np.zeros((51, 76))
counter = 0
while counter < 50:
    SobreRelax(V)
    counter += 1

V=np.arcsinh(np.transpose(V))
plt.imshow(V, origin='bottom', interpolation='nearest', extent=[-5, 5, -7.5, 7.5])
plt.colorbar()
plt.show()
