import matplotlib.pyplot as plt
import numpy as np

from projects.helper_modules import plot_helper as ph

# Basic Plot
# x = [0,1,2,3,4,5]
# y = [0,3,2,3,4,5]
#
# fig, ax = plt.subplots(1, 1)
# ax.set_title(label="My First Plot")
# ax.set_xlabel("X - Axis")
# ax.grid(visible=True)
# ax.plot(x, y)
# ax.set_xlim(0,5)
# ax.set_ylim(0,5)
# plt.show()

# Quiver

# Plot a vector
# def plot_2d_vector_base(ax, x, y, u, v, color):
#     for x_start, y_start, x_end, y_end in zip (x, y, u, v):
#         ax.quiver(x_start, y_start, x_end,y_end,  angles='xy', scale_units='xy', scale=1, color=color)

# m - 2D arrays of coordinates.
# Form: [[1,2],[3,4]]
# def plot_2d_vector_from_matrix(ax, m:NDArray, color):
#     x_start, y_start = np.zeros(m.size), np.zeros(m.size)
#     x_end, y_end = m[:,0], m[:,1]
#     plot_2d_vector_base(ax, x_start, y_start, x_end, y_end, color)

# I = np.linspace(0, 180, 10)
# SIN_I = np.sin(I)
# SIN_I_2 = 3 * SIN_I
# X_ZEROS = np.zeros_like(SIN_I_2)
# Y_ZEROS = np.zeros_like(SIN_I_2)
# U = np.ones_like(SIN_I_2)
fig , ax = plt.subplots()
# ax.quiver(X_ZEROS, Y_ZEROS, U,SIN_I_2,  angles='xy', scale_units='xy', scale=1)

test_arr = np.array([
    [1,2],
    [3,4]
])
scaler = np.array([
    [2,0],
    [0,2]
])
print("Original", test_arr)
scaled_test = test_arr @ scaler
print("Scaled", scaled_test)
ph.plot_2d_vector_from_matrix(ax, test_arr, "blue")
ph.plot_2d_vector_from_matrix(ax, scaled_test, "green")
print("x min/max", np.min(scaled_test[:,0]),np.max(scaled_test[:,0]))
print("y min/max", np.min(scaled_test[:,1]),np.max(scaled_test[:,1]))
# ax.set_xlim(np.min(scaled_test[:,0]),np.max(scaled_test[:,0]))
# ax.set_ylim(np.min(scaled_test[:,1]),np.max(scaled_test[:,1]))
ax.set_xlim(-10,20)
ax.set_ylim(-10,20)
plt.grid()
plt.show()
