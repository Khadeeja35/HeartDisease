import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Yes", "No"])
y = np.array([108829, 144851])

plt.xlabel("HighBp")
plt.bar(x, y)
plt.show()