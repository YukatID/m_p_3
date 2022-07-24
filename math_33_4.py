import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
def equations(p):
    x, y = p
    return (y - x**2 + 1, np.exp(x) - x*y +x -1)

x = np.linspace(-2,3,201)
plt.plot(x,(np.exp(x) +x - 1)/x)
plt.plot(x, x**2 - 1)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-1.5)
plt.grid(True)
plt.show()

xx = -1.5
yy = 1.5
print("Решение с точкой приближения: (",xx,";",yy,")")
x1, y1 = fsolve(equations,(xx,yy))
print ("x1=",x1,"; y1=",y1)
xx = 2.5
yy = 5.5
print("Решение с точкой приближения: (",xx,";",yy,")")
x2, y2 = fsolve(equations,(xx,yy))
print ("x2=",x2,"; y2=",y2)

print()

def ner(x,y):
    return np.exp(x)+x*(1-y)-1
print ("Выше мы нашли корни системы уравнений. Проверим найденные корни, подставив их в систему с уравнением и неравенством.")
print("y = x**2 – 1")
print ("exp(x) + x∙(1 – y) -1 > 0")
print("Решением системы будут корни, при котором выполняется неравенство (>0 ). Подставим и посчитаем:")
print("x1,y1:",ner(x1,y1))
print("x2,y2:",ner(x2,y2))