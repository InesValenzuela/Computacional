# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

#Lectura de datos y separación
datos = np.loadtxt('ny.txt')
x=datos[:,0]
y=datos[:,1]

#Definiendo la forma de la función
fitfunc = lambda p, x: p[0]*x + p[1]
errfunc = lambda p, x, y: fitfunc(p, x) - y 
p0 = [1, 1]

#Ajuste de la recta
p1, success = optimize.leastsq(errfunc, p0[:], args=(x, y)) 

#Graficando
time = np.linspace(x.min(), x.max(), 100)
plt.plot(x, y, "go", label="Datos") 
plt.plot(time, fitfunc(p1, time), "b-", label="Ajuste ineal")

plt.grid()
plt.legend()
plt.title("Temperaturas en New York")
plt.xlabel("Ano")
plt.ylabel("Temperatura")

plt.show()



