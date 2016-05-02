# -*- coding: utf-8 -*-
# MODELO CON TRATAMIENTO
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.ion()
plt.rcParams['figure.figsize'] = 10, 8

# PARAMETROS
P = 0       # Nacimientos en S
d = 0.0001  # Muertes en S
B = 0.0095  # Infecciones en S
G = 0.0001  # Resurrecciones de R a Z
A = 0.0001  # Destruccion en Z
rho = 0.5   # Conversion de I a Z
c = 0.3     # Curaciones de Z a S

# SOLUCION DEL SISTEMA
def f(y, t):
    Si = y[0]
    Ii = y[1]
    Zi = y[2]
    Ri = y[3]
  
    # Ecuaciones del modelo
    f0 = P - B*Si*Zi - d*Si + c*Zi
    f1 = B*Si*Zi - rho*Ii - d*Ii
    f2 = rho*Ii + G*Ri - A*Si*Zi - c*Zi
    f3 = d*Si + d*Ii + A*Si*Zi - G*Ri
    return [f0, f1, f2, f3]

# CONDICIONES INICIALES
S0 = 500                   # Poblacion S inicial
I0 = 5                     # Poblacion I inicial
Z0 = 0                      # Poblacion Z inicial
R0 = 0                      # Poblacion R inicial

y0 = [S0, I0, Z0, R0]   # Vector de condiciones iniciales

t  = np.linspace(0, 10, 1000)       

# SOLUCION DEL DES
soln = odeint(f, y0, t)
S = soln[:, 0]
I = soln[:, 1]
Z = soln[:, 2]
R = soln[:, 3]


# PARA GRAFICAR
plt.figure()
plt.plot(t, S, label='Vivos')
plt.plot(t, Z, label='Zombies')
plt.xlabel('Tiempo (dias)')
plt.ylabel('Población')
plt.title('Modelo con Tratamiento')
plt.legend(loc=0)





