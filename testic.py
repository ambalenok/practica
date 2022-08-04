import numpy as np
import matplotlib.pyplot as plt
x = np.arange(1, 2, 0.01)
plt.plot(x, 2*x**-2)
plt.grid(True)
plt.xlabel('X')
plt.title(r'$f(x)=2x^{-2}$')
plt.show()