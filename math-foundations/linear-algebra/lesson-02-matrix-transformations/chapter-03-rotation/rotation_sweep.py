import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

# Original vector
original_vector = np.array([1, 0])

# Create figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.grid(True)

# Plot handles
vector_line, = ax.plot([], [], 'r-', lw=2, label='Rotated Vector')
origin_line, = ax.plot([0, original_vector[0]], [0, original_vector[1]], 'k--', lw=1, label='Original Vector')
angle_label = ax.text(0.05, 1.2, '', fontsize=12)
ax.legend()

# Rotation matrix generator
def rotation_matrix(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])

# Animation initialization
def init():
    vector_line.set_data([], [])
    angle_label.set_text('')
    return vector_line, angle_label

# Frame update function
def animate(frame):
    theta = 2 * np.pi * frame / 180  # Convert frame to radians
    rot_mat = rotation_matrix(theta)
    rotated_vector = rot_mat @ original_vector
    vector_line.set_data([0, rotated_vector[0]], [0, rotated_vector[1]])
    angle_label.set_text(f'θ = {np.degrees(theta):.1f}°')
    return vector_line, angle_label

# Create animation
ani = animation.FuncAnimation(
    fig, animate, init_func=init, frames=180, interval=50, blit=True
)

# Save as GIF
ani.save("rotation_sweep.gif", writer=PillowWriter(fps=20))
print("GIF saved as 'rotation_sweep.gif'")