import numpy as np


Lx=10
Ly=15
h=0.2
N_pasos_x = Lx / h + 1
N_pasos_y = Ly / h + 1

phi=np.zeros( ( N_pasos_x , N_pasos_y ) )

print phi
