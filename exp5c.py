import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)

y = x ** 2

plt.plot(x, y, label='y = x²')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y = x²')

plt.grid(True)
plt.legend()

plt.show()
