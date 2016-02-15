# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Lectura de datos y separación
datos = np.loadtxt('pa.txt')
x=datos[:,0]
y=datos[:,1]

#Definiendo la forma de la función
def f(x, a, b, c):
    return a * np.exp(-b * x) + c
    
    
#Ajuste exponencial    
popt, pcov = curve_fit(f,x,y)

#Graficando
plt.plot(x, y, "mo", label='Datos')
plt.plot( x, f(x, *popt), "b-", label='Ajuste Exponencial')

plt.grid()
plt.legend()
plt.title("Presion Atmosferica vs. Altitud")
plt.xlabel("Altitud")
plt.ylabel("Presion")

plt.show()