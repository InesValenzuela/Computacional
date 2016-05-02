from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

#Movimiento Fisico del Pendulo

class DoublePendulum:

    def __init__(self,
                 init_state = [ 120 ,0, 0, 0],
                 L1=1.0,     # Largo del pendulo en metros
                 L2=0.0,     # Ponemos 0 el largo del segundo pendulo
                 M1=1.0,     # Masa del primer pendulo
                 M2=1.0,     # Masa del segundo pendulo
                 G=9.8,      # Aceleracion gravitacional
                 origin=(0, 0)): 
        self.init_state = np.asarray(init_state, dtype='float')
        self.params = (L1, L2, M1, M2, G)
        self.origin = origin
        self.time_elapsed = 0

        self.state = self.init_state * np.pi / 180.
    
    def position(self):
        
        (L1, L2, M1, M2, G) = self.params

        x = np.cumsum([self.origin[0],
                       L1 * sin(self.state[0])])
        y = np.cumsum([self.origin[1],
                       -L1 * cos(self.state[0])])
        return (x, y)

  
    def dstate_dt(self, state, t):
    
        (M1, M2, L1, L2, G) = self.params
    
        dydx = np.zeros_like(state)
        dydx[0] = state[1]
        dydx[2] = state[3]

        cos_delta = cos(state[2] - state[0])
        sin_delta = sin(state[2] - state[0])

        den1 = (M1 + M2) * L1 - M2 * L1 * cos_delta * cos_delta
        dydx[1] = (M2 * L1 * state[1] * state[1] * sin_delta * cos_delta
                   + M2 * G * sin(state[2]) * cos_delta
                   + M2 * L2 * state[3] * state[3] * sin_delta
                   - (M1 + M2) * G * sin(state[0])) / den1
        
        return dydx

    
    def step(self, dt):
        """execute one time step of length dt and update state"""
        self.state = integrate.odeint(self.dstate_dt, self.state, [0, dt])[1]
        self.time_elapsed += dt
        
        return self.state
    
        
# Estado inicial
pendulum = DoublePendulum([170, 40, 0., 0.0])   #theta1, omega1, theta2, omega2
dt = 1./30 


# Figuara y animacion

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                     xlim=(-2, 2), ylim=(-2, 2)) 
ax.grid()

line, = ax.plot([], [], 'o-', lw=2, color='magenta')
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)



def init():
    """initialize animation"""
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text


def animate(i):
    """perform animation step"""
    global pendulum, dt
    pendulum.step(dt)
    
    line.set_data(*pendulum.position())
    time_text.set_text('tiempo = %.1f' % pendulum.time_elapsed)
    return line, time_text
    
  
from time import time
t0 = time()
animate(0)
t1 = time()
interval = 1000 * dt - (t1 - t0)

ani = animation.FuncAnimation(fig, animate, frames=80,
                              interval=interval, blit=True, init_func=init)

ani.save('pendulo0', writer='ffmpeg')


plt.show()

#===========================================================================

# ESPACIO FASE

def pend(y, t, b, c):
     theta, omega = y
     dydt = [omega, -b*omega - c*np.sin(theta)]
     return dydt
     
#Parametros
b = 0.0         #Friccion
g = 9.8         #Aceleracion gravitacional
l = 4.5         #longitud de la cuerda
c = g/l


y0 = [(0*np.pi)/180, 15.0]      #Angulo inical, velocidad angular

t = np.linspace(0, 20, 100) 

from scipy.integrate import odeint
sol = odeint(pend, y0, t, args=(b, c))


#Para crear los archivos:

file = open("90.txt","w")
file.close()
file = open('90.txt','r')

#Para crear archivo a partir de los datos obtenidos
np.savetxt("90.txt", sol)

file = open("90.txt","r")
print file.read()

import matplotlib.pyplot as plt 
import numpy as np


data = np.loadtxt('90.txt')

x1=data[:,0]    #velocidad angular
y1=data[:,1]    #posicion angular


x11 = x1.astype(np.float)       #velocidad
y11 = y1.astype(np.float)      #posicion


#Animacion del espacio fase

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation



class SubplotAnimation(animation.TimedAnimation):
    def __init__(self):
        fig = plt.figure()
    
        ax1 = fig.add_subplot(1, 1, 1) 
        

        
        #Funcion a graficar
        self.t = np.linspace(0, 80, 300)#tiempo inicial ,velocidad inicial, puntos
        self.x = x11               #funcion eje x
        self.y = y11               #funcin eje y
        self.z = 5 * self.t

        
        #Caracteristicas animacion eje xy
        
        ax1.set_xlabel('Posicion angular')
        ax1.set_ylabel('Velocidad angular')
        self.line1 = Line2D([], [], color='pink')
        self.line1a = Line2D([], [], color='magenta', linewidth=2)
        self.line1e = Line2D(
            [], [], color='magenta', marker='o', markeredgecolor='b')
        ax1.add_line(self.line1)
        ax1.add_line(self.line1a)
        ax1.add_line(self.line1e)
        ax1.set_xlim(-4, 4)
        ax1.set_ylim(-8, 8)
      

    
        animation.TimedAnimation.__init__(self, fig, interval=115, blit=115)

    def _draw_frame(self, framedata):
        i = framedata
        head = i - 1
        head_len = 10
        head_slice = (self.t > self.t[i] - 1.0) & (self.t < self.t[i])

        self.line1.set_data(self.x[:i], self.y[:i])
        self.line1a.set_data(self.x[head_slice], self.y[head_slice])
        self.line1e.set_data(self.x[head], self.y[head])

        self._drawn_artists = [self.line1, self.line1a, self.line1e,
                               #self.line2, self.line2a, self.line2e,
                               #self.line3, self.line3a, self.line3e
                               ]

    def new_frame_seq(self):
        return iter(range(self.t.size))

    def _init_draw(self):
        lines = [self.line1, self.line1a, self.line1e,
                 #self.line2, self.line2a, self.line2e,
                 #self.line3, self.line3a, self.line3e
                 ]
        for l in lines:
            l.set_data([], [])

ani = SubplotAnimation()
#ani.save('pendulo0F', writer='ffmpeg')


plt.show()




