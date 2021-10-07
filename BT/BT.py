import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,4 *np.pi, 0.1)
y_sin = np.sin(x)

y_cos = np.cos(x)

plt.plot(x,y_sin)
plt.plot(x,y_cos)
plt.xtick('trục X')
plt.ylabel('trục Y')
plt.title('Hàm Sin Và Cos trong khoảng 0 đến 4 pi')
plt.legend(['SIN(x)', 'COS(x)'])
plt.show()


