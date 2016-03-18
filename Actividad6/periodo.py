#BIBLIOTECAS
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

#CONSTANTES

g=9.8 #aceleracion gravitacional
l= 2  #longitud del pendulo en metros
n= 500 #numero de angulos
ep=0.001 # error para que no divida entre 0

#variacion del angulo
theta_0 =np.linspace(ep, (np.pi)-ep, n)

#RESULTADOS DE LA INTEGRAL
I = [0 for i in range(n)]
err = [0 for i in range(n)]
Tr = [0 for i in range(n)]

#PARA ANGULOS PEQUENOS
T0 = 2.0 * np.pi*np.sqrt(l/g)

#RESOLVER LA INTEGRAL
inte = lambda x, t : 1.0 /(np.sqrt(np.cos(x)-np.cos(t)))

for i in range(n):
    theta_00 = theta_0[i]
    I[i] , err [i] = quad(inte, 0, theta_00, args=(theta_00))
    Tr[i] = 4*np.sqrt(l/(2*g)) * I[i]
   
 
#Periodo real entre el periodo para angulos pequenos       
raz=Tr/T0

theta_g = (theta_0*180.0)/np.pi #Transformacion a Grados


#PARA GRAFICAR
plt.plot(theta_g, raz, color="m")
plt.title("Error Relativo")
plt.xlabel("Angulo en grados")
plt.ylabel("Razon entre los periodos")
plt.axis([0,90,1,1.20])
plt.show()