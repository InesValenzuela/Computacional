# -*- coding: utf-8 -*-
# MODELO CON CUARENTENA
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.ion()
plt.rcParams['figure.figsize'] = 10, 8

#PARAMETROS

P = 0           # Nacimientos de S
d = 0.0001      # Muertes de S
B = 0.0095      # Infecciones de S
G = 0.0001      # Resurreciones de R a Z
A = 0.0001      # Destruccion de Z
rho=1           # Conversion de I a Z
k=0.001         # Ingreso de I a Q
sigma=0.009     # Ingreso de Z a Q
Ga=0.004        # Muertes en Q



# SOLUCION DEL SISTEMA
def f(y, t):
    Si = y[0]
    Ii = y[1]
    Zi = y[2]
    Ri = y[3]
    Qi = y[4]
    
    # Ecuaciones del modelo
    f0 = P - B*Si*Zi - d*Si
    f1 = (B*Si*Zi)-(rho*Ii)-(d*Ii)-(k*Ii)
    f2 = (rho*Ii) + (G*Ri)-(A*Si*Zi)-(sigma*Zi)
    f3 = (d*Si) + (d*Ii) + (A*Si*Zi)-(G*Ri)+(Ga*Qi)
    f4 = (k*Ii)+(sigma*Zi)-(Ga*Qi)
    
    return [f0, f1, f2, f3, f4]

# CONDICIONES INICIALES
S0 = 500.                   # Poblacion S inicial
Z0 = 0.                     # Poblacion Z inicial
R0 = 0.                     # Poblacion R inicial
I0 = 100.                   # Poblacion I inicial
Q0 = 130.                   # Poblacion Q inicial
y0 = [S0, Z0, R0, I0, Q0]   # Vector de condiciones iniciales

t  = np.linspace(0, 10., 1000)       

# SOLUCION DEL DEs
soln = odeint(f, y0, t)
S = soln[:, 0]
I = soln[:, 1]
Z = soln[:, 2]
R = soln[:, 3]
Q = soln[:, 4]

# PARA GRAFICAR
plt.figure()
plt.plot(t, S, label='Vivos')
plt.plot(t, Z, label='Zombies')
plt.xlabel('Tiempo (dias)')
plt.ylabel('Población')
plt.title('Modelo con Cuarentena')
plt.legend(loc=0)


# In[14]:




# In[ ]:



