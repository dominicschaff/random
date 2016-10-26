import numpy as np
import matplotlib.pyplot as plt
from poly_fit import poly_fit

def draw():
    xdata = np.array([0.0,1.0,2.0,2.5,3.0])
    ydata = np.array([2.9,3.7,4.1,4.4,5.0])
    a = poly_fit(xdata,ydata, 1)
    x_approx = np.array([0.0, 3.0])
    y_approx = np.zeros(2)
    for i in xrange(len(x_approx)):
        y_approx[i] += a[0] + a[1]*x_approx[i]

    plt.plot(xdata,ydata, 'ro', x_approx, y_approx, 'b-')
    plt.show()

if __name__ == '__main__':
    draw()