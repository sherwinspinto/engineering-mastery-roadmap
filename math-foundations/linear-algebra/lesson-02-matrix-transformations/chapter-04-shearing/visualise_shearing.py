import matplotlib.pyplot as plt
import numpy as np

# Apply A = [[1,1],[0,1]] to [1,0], [0,1], [1,1]
shearing_v = np.array([[1,1],[0,1]])

v_1 = np.array([0,1])
vs_1 = shearing_v @ v_1.T

fig, ax = plt.subplots()
ax.quiver([0],[0], [v_1[0]], [v_1[1]], angles='xy', scale_units='xy', scale=1, color='blue')
ax.quiver([0],[0], [vs_1[0]], [vs_1[1]], angles='xy', scale_units='xy', scale=1, color='red')
ax.grid()
ax.set_aspect('equal')
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
plt.show()

