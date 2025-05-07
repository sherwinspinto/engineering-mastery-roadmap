import matplotlib as plt
import numpy as np
from numpy.typing import NDArray

def plot_2d_vector_base(ax, x_start, y_start, x_end, y_end, color):
    ax.quiver(x_start, y_start, x_end,y_end,  angles='xy', scale_units='xy', scale=1, color=color)

def plot_2d_vector_from_matrix(ax, m:NDArray, color):
    x_end, y_end = m[:,0], m[:,1]
    x_start, y_start = np.zeros(x_end.size), np.zeros(y_end.size)
    plot_2d_vector_base(ax, x_start, y_start, x_end, y_end, color)


# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import Normalize
# from matplotlib.cm import ScalarMappable
#
# # Example data
# x = np.linspace(0, 2 * np.pi, 10)
# y = np.sin(x)
# u = np.cos(x)
# v = np.sin(x)
#
# # Color values for each arrow (e.g., magnitude)
# magnitudes = np.sqrt(u**2 + v**2)
#
# # --- Plot 1: Colors mapped by magnitude ---
# fig, ax = plt.subplots(figsize=(8, 6))
#
# norm = Normalize(vmin=magnitudes.min(), vmax=magnitudes.max())
# cmap = plt.cm.viridis
# colors = cmap(norm(magnitudes))
#
# q = ax.quiver(x, y, u, v, color=colors, scale=5)
#
# sm = ScalarMappable(norm=norm, cmap=cmap)
# sm.set_array([])  # Needed for colorbar
# cbar = fig.colorbar(sm, ax=ax, label='Magnitude')
# ax.set_title('Quiver plot with colors mapped by magnitude')
# plt.show()
#
# # --- Plot 2: Explicit colors for each arrow ---
# explicit_colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'cyan', 'magenta']
#
# plt.figure(figsize=(8, 6))
# plt.quiver(x, y, u, v, color=explicit_colors, scale=5)
# plt.title('Quiver plot with explicit colors')
# plt.show()
