import numpy as np
import matplotlib.pyplot as plt
import math
def plot_ellipsoid(a,b):
    x=[]
    y=[]
    x = np.linspace(-a, a, 512, endpoint=True)
    y = np.sqrt((1-x**2/a**2)*b**2)
    plt.plot(x, y, marker = "o")
    plt.plot(x, -y, marker = "o")
    plt.gca().set_aspect('equal')
    plt.show()

def plot_circle(R):
    x=[]
    y=[]
    x = np.linspace(-R, R, 512, endpoint=True)
    y = np.sqrt(-(x*x) + R*R)
    plt.plot(x, y, marker = "o")
    plt.plot(x, -y, marker = "o")
    plt.gca().set_aspect('equal')
    plt.show()

def plot_hyperboloid(a,b):
    x=[]
    y=[]
    x = np.linspace(-a*3, a*3, 512, endpoint=True)
    y = np.sqrt((x**2/a**2 - 1)*b**2)
    plt.plot(x, y, marker = "o")
    plt.plot(x, -y, marker = "o")
    plt.show()

plot_circle(1)
plot_ellipsoid(3,2)
plot_hyperboloid(2,2)