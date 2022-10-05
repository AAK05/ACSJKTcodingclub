import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,20,21)
y = [5*i+3 for i in x]
plt.plot(x,y,marker=".",label="y=5x+3")
plt.legend()
plt.grid()
plt.show()