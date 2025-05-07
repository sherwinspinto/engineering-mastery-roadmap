import numpy as np
import matplotlib.pyplot as plt

# Define identity matrix
det_1 = np.array([[1, 0], [0, 1]])
det_neg_1 = np.array([[0, 1], [1, 0]])

# Define a vector [1,0]
original_v = np.array([4,1])
v = original_v @ det_1
fig, ax = plt.subplots()
ax.quiver(0,0,v[0],v[1], angles='xy', scale_units='xy', scale=1, label='Original')
q = original_v @ det_neg_1
print("Matrix multiplication by matrix with det = -1", q)
ax.quiver(0,0,q[0],q[1], angles='xy', scale_units='xy', scale=1, color='green', label='Reflected')
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
ax.grid()
ax.legend()
plt.show()

