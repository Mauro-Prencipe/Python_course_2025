from exercise_4_complete import Mini
import numpy as np
import matplotlib.pyplot as plt

def polyfun(x):
    coef=np.array([2.5, -10., 14., -7., 1.7])
    
    return np.polyval(coef, x)


x_list=np.linspace(-0.5, 1.5, 100)
y_list=polyfun(x_list)

plt.figure(figsize=(3,2))
plt.plot(x_list,y_list)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

Mini.set_expand(1.2)
Mini.set_precision(1e-9)
Mini.info()
Mini.findmin(polyfun, 0.5)
