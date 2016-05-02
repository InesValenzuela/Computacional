# -*- coding: utf-8 -*-

# MODELO BASICO SIN ZOMBIES
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.ion()
plt.rcParams['figure.figsize'] = 10, 8


#PARAMETROS
P = 0       # Nacimientos de S
d = 0.0001  # Muertes de S
B = 0.0000  # Infeccion de S
G = 0.0001  # Resurreccion de R a Z
A = 0.0005  # Destruccion de Z

# SOLUCION DEL SISTEMA
def f(y, t):
    Si = y[0]
    Zi = y[1]
    Ri = y[2]
    
    # Ecuaciones del modelo
    f0 = P - B*Si*Zi - d*Si
    f1 = B*Si*Zi + G*Ri - A*Si*Zi
    f2 = d*Si + A*Si*Zi - G*Ri
    return [f0, f1, f2]
    

# CONDICIONES INICIALES

S0 = 500.                   # Poblacion S inicial
Z0 = 0                      # Poblacion Z inicial
R0 = 0                      # Poblacion R inicial
y0 = [S0, Z0, R0]           # Vector de condiciones iniciales

t  = np.linspace(0, 30., 1000)       

# SOLUCION DEL DEs
soln = odeint(f, y0, t)
S = soln[:, 0]
Z = soln[:, 1]
R = soln[:, 2]

# PARA GRAFICAR
plt.figure()
plt.plot(t, S,'p', label='Vivos')
plt.plot(t, Z, 'p', label='Zombies')
plt.xlabel('Tiempo en dias')
plt.ylabel('Población')
plt.title('Modelo basico sin zombies')
plt.legend(loc=0)





