import matplotlib.pyplot as plt
import numpy as np

x = np.array(["HighBp", "HighChol"])
y = np.array([108829, 107591])

plt.bar(x, y)
plt.show()