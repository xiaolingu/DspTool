import numpy as np
from numpy import matlib as nb 
import matplotlib as mpl 
from matplotlib import pyplot
def pulsint(x):
    return np.sum(x, 0)
npulse = 10
x = nb.repmat(np.sin(2*np.pi*np.arange(0, 100)/100), npulse, 1)
y = 0.1 * np.random.randn(npulse, 100)
pyplot.plot(pulsint(x + y))
pyplot.ylabel('Magnitude')
pyplot.show()