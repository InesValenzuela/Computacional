# -*- coding: utf-8 -*-
# MOODELO CON INFECCION LATENTE
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.ion()
plt.rcParams['figure.figsize'] = 10, 8

#PARAMETROS

P = 0       # Nacimientos de S
d = 0.0001  # Muertes de s
B = 0.0095  #Infecciones de S
G = 0.0001  # Resurreccion de R a S
A = 0.0001  # Destruccion de Z
rho = 0.5   #Conversion de I a Z

# SOLUCION DEL SISTEMA
def f(y, t):
    Si = y[0]
    Ii = y[1]
    Zi = y[2]
    Ri = y[3]
  
    # Ecuaciones del modelo
    f0 = P - B*Si*Zi - d*Si
    f1 = B*Si*Zi - rho*Ii - d*Ii
    f2 = rho*Ii + G*Ri - A*Si*Zi
    f3 = d*Si + d*Ii + A*Si*Zi - G*Ri
    return [f0, f1, f2, f3]

# CONDICIONES INICIALES
S0 = 500                   # Poblacion S inicial
I0 = 1                     #Poblacion I inicial
Z0 = 0                     # Poblacion Z inicial
R0 = 20                    # Poblacion R inicial
y0 = [S0, I0, Z0, R0]      # vector de condiciones iniciales

t  = np.linspace(0, 10., 1000)       

# SOLUCION DEL DEs
soln = odeint(f, y0, t)
S = soln[:, 0]
I = soln[:, 1]
Z = soln[:, 2]
R = soln[:, 3]


# PARA GRAFICAR
plt.figure()
plt.plot(t, S, label='Vivos')
plt.plot(t, Z, label='Zombies')
plt.xlabel('Tiempo en dias')
plt.ylabel('Población')
plt.title('Modelo con Infeccion Latente')
plt.legend(loc=0)

