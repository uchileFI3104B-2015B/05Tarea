'''
metodos que no son utiles, pero podrian serlo. estorban en el codigo central
mejor guardarlos aca
'''



    for j in range(1, 12):
        for i in range(1, N_x -1):
            phi_n[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_n[i-1, j] +
                                       phi[i, j+1] + phi_n[i, j-1] )

    for j in range(12, 14):
        for i in range(1, N_x):
            phi_n[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_n[i-1, j] +
                                       phi[i, j+1] + phi_n[i, j-1] )

        for i in range(1, 11):
            phi_n[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_n[i-1, j] +
                                       phi[i, j+1] + phi_n[i, j-1] )
        for i in range(41, N_x):
            phi_n[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_n[i-1, j] +
                                       phi[i, j+1] + phi_n[i, j-1] )

        for j in range(12, 13): #redundante, pero me sirve para ordenar mi idea
            for i in range(11, 41):

        for j in range(13, 14): #redundante, pero me sirve para ordenar mi idea
            for i in range(11, 41):

    for j in range(14, 17):
        for i in range(1, 12):
            phi_n[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_n[i-1, j] +
                                       phi[i, j+1] + phi_n[i, j-1] )
        for i in range(12, 38):
            phi_n[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_n[i-1, j] +
                                       phi[i, j+1] + phi_n[i, j-1] +
                                       h**2. * r(i, j, Lx, Ly, h)))
        for i in range(38, N_x -1):
            phi_n[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_n[i-1, j] +
                                       phi[i, j+1] + phi_n[i, j-1] )
    for j in range(17, N_y - 1):
        for i in range(1, N_x -1):
            phi_n[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_n[i-1, j] +
                                       phi[i, j+1] + phi_n[i, j-1] )




    for i in range(1, N_x - 1):
        for j in range(1, 12):
            phi_n[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_n[i-1, j] +
                                       phi[i, j+1] + phi_n[i, j-1] ))
        for j in range(14, N_y - 1):
            phi_n[i, j] = ((1 - w) * phi[i, j] +
                              w / 4 * (phi[i+1, j] + phi_n[i-1, j] +
                                       phi[i, j+1] + phi_n[i, j-1] ))
