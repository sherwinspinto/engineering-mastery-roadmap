import matplotlib.pyplot as plt
import numpy as np

# Plot a vector v from origin in 2D
# v = np.array([[0,2]])
# fig, ax = plt.subplots()
# ax.quiver([[0,0]],[[0,0]],[[1,2]],[[2,-3]], angles='xy', scale_units='xy', scale=1, color='r')
# ax.set_xlim(-5,5)
# ax.set_ylim(-5, 5)
# ax.legend("speed")
# ax.set_xlabel("x-label")
# ax.set_ylabel("y-label")
# ax.grid()
# ax.set_aspect("equal")
# plt.show()

# Relace to linear combination and span
import numpy as np
import matplotlib.pyplot as plt

def plot_vectors(ax, vectors, colors, labels, title, target=None):
    origin = np.zeros(2)
    for v, color, label in zip(vectors, colors, labels):
        ax.quiver(*origin, *v, angles='xy', scale_units='xy', scale=1, color=color, label=label)
    if target is not None:
        ax.quiver(*origin, *target, angles='xy', scale_units='xy', scale=1, color='black', dashes='-', label='target')
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 5)
    ax.set_aspect('equal')
    ax.grid(True)
    ax.set_title(title)
    ax.legend()

# === 1. Linearly Dependent Vectors ===
v1_dep = np.array([2, 4])
v2_dep = np.array([1, 2])     # v2_dep = 0.5 * v1_dep
w_dep = np.array([1, 3])      # NOT in span of v1_dep and v2_dep

# === 2. Linearly Independent Vectors ===
v1_indep = np.array([2, 1])
v2_indep = np.array([-1, 1])
w_indep = np.array([1, 3])    # IS in span of v1_indep and v2_indep

# === Plotting ===
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plot dependent case
plot_vectors(
    ax1,
    [v1_dep, v2_dep],
    ['blue', 'orange'],
    ['v1 (dep)', 'v2 (dep)'],
    'Linearly Dependent Vectors',
    target=w_dep
)

# Plot independent case
plot_vectors(
    ax2,
    [v1_indep, v2_indep],
    ['green', 'purple'],
    ['v1 (indep)', 'v2 (indep)'],
    'Linearly Independent Vectors',
    target=w_indep
)

plt.tight_layout()
plt.show()