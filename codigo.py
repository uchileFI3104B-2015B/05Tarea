import numpy as np
import matplotlib.pyplot as plt
from _futuro_ import division

#Main

#Setup
Lx = 10
Ly = 15
N_pasosx = 11
N_pasosy= 16
hx = Lx / (N_pasosx - 1)
hy = Ly / (N_pasosy - 1)


V = np.zeros((N_pasosy, N_pasosx))
V_next= np.zeros((N_pasosy, N_pasosx))

print(V)
