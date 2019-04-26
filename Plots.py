import pylab
import math
import numpy


def plot_45deg_line():
    pylab.figure(1)
    pylab.plot([1, 2, 3, 4], [1, 2, 3, 4])
    pylab.show()


def plot_sine():
    pylab.figure(1)
    x_vals = []
    y_vals = []
    for i in numpy.arange(0, 10, 0.1):
        x_vals.append(i)
        y_vals.append(math.sin(i))
    pylab.plot(x_vals, y_vals)
    pylab.show()
