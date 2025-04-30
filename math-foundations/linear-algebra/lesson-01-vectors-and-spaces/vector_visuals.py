import matplotlib.pyplot as plt
import numpy as np

# Plot a vector v from origin
# v = [1,2]
# origin = [0], [0]
#
# plt.quiver(*origin, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='r')
# plt.xlim(-5, 5)
# plt.ylim(-5, 5)
# plt.grid()
# plt.gca().set_aspect('equal')
# plt.show()

# Define grid
# X, Y = np.meshgrid(np.arange(-2, 3, 1), np.arange(-2, 3, 1))
#
# # Define vector components with the correct shape (5x5 grid)
# U = np.ones_like(X)  # U components all set to 1
# V = np.array([[1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1]])
#
# fig, ax = plt.subplots()
# ax.quiver(X, Y, U, V)
#
# ax.set_xlim(-3, 3)
# ax.set_ylim(-3, 3)
# plt.show()