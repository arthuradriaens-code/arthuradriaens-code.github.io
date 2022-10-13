import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,500,10000)
y = (2.2*(10**(-2)))**2 + (0.978**2)*(1 - 0.851004*np.sin(0.0433*x)**2)
#y = np.sin(0.0433*x)**2
plt.xlabel("L(Km)")
plt.ylabel("$P_{ee}$")
plt.title("Probability of no oscillation")
plt.plot(x,y)
plt.show()
