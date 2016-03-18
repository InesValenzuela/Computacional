#==========================================================
# ESPACIO FASE DEL PENDULO                                
# FISICA COMPUTACIONAL                                    
# MARIA INES VALENZUELA CARRILLO                          
#==========================================================

#Bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


#Definicion de la ecuacion 
def pend(y, t, b, c):
        theta, omega = y
        dydt = (omega, -b*omega - c*np.sin(theta))
        return dydt
        
    
#Parametros
b = 0            #friccion
g= 9.8           # aceleracion gravitacional
l=1              #longitud del pendulo
c=g/l
t = np.linspace(0.0,20,500)  #intervalo de tiempo


#Condiciones iniciales
X_f1 =np.array([-70.0*np.pi,20])
X_f2 =np.array([-2.0*np.pi,0.0]) 


values1 =np.linspace(-1,1,70)                
values2 =np.linspace(-1,1,50)                
vcolors1 = plt.cm.Blues(np.linspace(1.0, 1.0, len(values1)))  # colores1 para cada trayectoria
vcolors2 = plt.cm.PuRd(np.linspace(0.7, 0.7, len(values2)))  # colores2 para cada trayectoria

plt.figure(2)


#Trayectorias superiores e inferiores
for v1, col1 in zip(values1, vcolors1):
    y1 = v1 * X_f1                                
    X1 = odeint(pend, y1, t, args=(b,c))         
    plt.plot( X1[:,0], X1[:,1], lw=1.5*v1, color=col1 )

#Trayectorias centrales                              
for v2, col2 in zip(values2, vcolors2):
    y2 = v2 * X_f2                                 
    X2 = odeint(pend, y2, t, args=(b,c))           
    plt.plot( X2[:,0], X2[:,1], lw=1.5*v2, color=col2 )


#Para graficar
plt.title('Trayectorias')
plt.xlabel('Angulo')
plt.ylabel('Velocidad Angular')
plt.grid()
plt.xlim(-3.0*np.pi,3.0*np.pi)
plt.ylim(-10,10)


plt.show()