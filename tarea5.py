import matplotlib.pyplot as plt
import numpy as np
def N(x, y):
    if x < -1.5:
        return x, y
    elif x > 1.5:
        return x, y
    elif x >= -1.5 and x < -0.5:
        if y >= 0.5 and y < 2.5:
            return x, y
        else:
            return 0, 0
    elif x >= -0.5 and x < 0.5:
        if y >= -1 and y < 1:
            return x, y
        else:
            return 0, 0
    elif x >= 0.5 and x < 1.5:
        if y >= -2.5 and y < -0.5:
            return x, y
        else:
            return 0, 0
    else:
        return 0, 0
h = 0.02
X = np.linspace(-2.5, 2.5, 251).tolist()
Y = np.linspace(-3.5, 3.5, 351).tolist()
Z = []
Letra = []
LetraX = []
LetraY = []
for a in range(len(X)):
    Z.append([])
for a in range(len(X)):
    for b in range(len(Y)):
        Z[a].append((X[a], Y[b]))

for a in range(len(X)):
    for b in range(len(Y)):
        L = N(Z[a][b][0], Z[a][b][1])
        Letra.append((L[0], L[1]))
        
for a in Letra:
    LetraX.append(a[0])
    LetraY.append(a[1])
    
plt.plot(LetraX, LetraY, 'o')
plt.xlim(-5, 5)
plt.ylim(-7.5, 7.5)
plt.show()
