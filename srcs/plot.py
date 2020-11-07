import numpy as np
import matplotlib.pyplot as plt


def poly_plot_deg_2(poly, res):
    x = np.linspace(-10, 10, num=100)
    y = []
    for i in range(len(x)):
        y.append(poly[2] * x[i] ** 2 + poly[1] * x[i] + poly[0])

    plt.figure('ComputerV1')
    plt.axvline()
    plt.axhline()
    plt.plot(x, y, 'y')
    plt.plot(res, [0 for i in range(len(res))], 'ro')
    plt.grid()
    plt.show()


def poly_plot_deg_1(poly, res):
    x = np.linspace(-10, 10, num=100)
    y = []
    for i in range(len(x)):
        y.append(poly[1] * x[i] + poly[0])

    plt.figure('ComputerV1')
    plt.axvline()
    plt.axhline()
    plt.plot(x, y, 'y')
    plt.plot(res, [0], 'ro')
    plt.grid()
    plt.show()
