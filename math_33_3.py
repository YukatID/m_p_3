import numpy as np
import matplotlib.pyplot as plt
def polarToDecart(a,R):
    return (R*np.cos(a), R*np.sin(a))

aa = np.pi/4
rr = 1
print ("Полярные координаты:", "угол", aa,"радиус",rr)
print("Перевод в декартовы координаты:",polarToDecart(aa,rr))
R=3
x = np.linspace(-R, R, 512, endpoint=True)
y = np.sqrt(-(x * x) + R * R)
plt.polar(x,y)
plt.show()
x = np.linspace(0,5,100)
y = 2*x+2
# plt.plot(x,y)
plt.polar(x,y)
plt.gca().set_aspect('equal')
plt.show()