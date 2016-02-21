# -*- coding: utf-8 -*-
#Soluución péndulo simple
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Para definir las ecuaciones
def pend(y, t, b, c):
        theta, omega = y
        dydt = (omega, -b*omega - c*np.sin(theta))
        return dydt
    
#Parametros    
b = 8
g= 9.8
l=2
c=g/l

#Condiciones iniciales
y0 = [np.pi/4 , 2 ]

#Intervalo de tiempo
t = np.linspace(0, 20, 1000)

#Para generar la solución 
sol = odeint(pend, y0, t, args=(b,c))

#Para graficar
plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, sol[:, 1], 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()