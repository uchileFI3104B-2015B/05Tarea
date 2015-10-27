def una_iteracion(V, V_next, N_pasosx, N_pasosy, h, w=1.):
    #Iteracion para la caja
    for i in range(1, int(N_pasosx)-1):
            #arriba
            for j in range(1, 11):
                V_next[i, j] = ((1 - w) * V[i, j] +
                                  w / 4 * (V[i+1, j] + V_next[i-1, j] +
                                           V[i, j+1] + V_next[i, j-1] +
                                           h**2 * rho(i, j, h)))
            #abajo
            for j in range(14, int(N_pasosy)-1):
                V_next[i, j] = ((1 - w) * V[i, j] +
                                  w / 4 * (V[i+1, j] + V_next[i-1, j] +
                                           V[i, j+1] + V_next[i, j-1] +
                                           h**2 * rho(i, j, h)))

    for j in range(11,14):
        #izq
        for i in range(1,10):
            V_next[i, j] = ((1 - w) * V[i, j] +
                                  w / 4 * (V[i+1, j] + V_next[i-1, j] +
                                           V[i, j+1] + V_next[i, j-1] +
                                           h**2 * rho(i, j, h)))
            #der
        for i in range(41,int(N_pasosx)-1):
            V_next[i, j] = ((1 - w) * V[i, j] +
                              w / 4 * (V[i+1, j] + V_next[i-1, j] +
                                       V[i, j+1] + V_next[i, j-1] +
                                       h**2 * rho(i, j, h)))


    #Condicion derivativa
    for i in range(10,41):
        for j in range(11,12):
            #abajo
            V_next[i,j] =  ((1 - w) * V[i, j] +
                          w / 3 * (V[i+1, j] + V_next[i-1, j] +
                                   V[i, j-1] + h**2 * rho(i, j, h) + h*(-1.)))
        for j in range(13,14):
            #arriba
            V_next[i,j] =  ((1 - w) * V[i, j] +
                          w / 3 * (V[i+1, j] + V_next[i-1, j] +
                                   V[i, j-1] + h**2 * rho(i, j, h) + h*(1.)))
    #en la linea neumann
    for j in range(12,13):
        for i in range(10,41):
            V_next[i,j] = V_next[i,j-1]+h*(1.)




una_iteracion(V, V_next, N_pasosx, N_pasosy, h, w=1.)
counter = 1
while counter < 10: #and no_ha_convergido(phi, phi_next, tolerancia=1e-7):
    V = V_next.copy()
    una_iteracion(V, V_next, N_pasosx, N_pasosy, h, w=1)
    counter += 1

print("counter = {}".format(counter))



V_next_traspuesta=V_next.transpose()

fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-1, 1, N_pasosx)
y = np.linspace(-1, 1, N_pasosy)
X, Y = np.meshgrid(x, y)
ax.plot_surface(X, Y, V_next_traspuesta, rstride=1, cstride=1)
fig.show()

fig2 = plt.figure(2)
fig2.clf()
ax2 = fig2.add_subplot(111)
ax2.imshow(V_next_traspuesta, origin='bottom', interpolation='nearest')
fig2.show()
