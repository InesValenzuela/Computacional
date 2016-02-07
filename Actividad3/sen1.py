import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Original "data set" --- 21 random numbers between 0 and 1.
x00 = np.random.random(10)
x0=3*x00
y0 = np.sin(2*x0)

plt.plot(x0, y0, 'o', label='Data')

# Array with points in between those of the data set for interpolation.
x=np.linspace(min(x0), max(x0), 101)

# Available options for interp1d
options = ('slinear', 'quadratic', 'cubic')

for o in options:
    f = interp1d(x0, y0, kind=o)    # interpolation function
    plt.plot(x, f(x), label=o)      # plot of interpolated data

plt.legend()
plt.show()