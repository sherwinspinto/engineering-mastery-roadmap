import numpy as np
import matplotlib.pyplot as plt

from python_journey.helper_modules.linear_algebra_helper import rotate_2d_matrix

# Visualise the rotation of a vec = [1,0]
o_v = np.array([1,0])

# O degree rotation
zero_rotation_theta = 0

# Zero rotation operation
zero_rotation_v = rotate_2d_matrix(o_v, zero_rotation_theta)

# rotation to be applied to input o_v = [1,0]
ninety_rotation_theta = np.pi/2

# Rotating input vector o_v by 90 degrees
ninety_rotation_v = rotate_2d_matrix(o_v, ninety_rotation_theta)

# rotation to be applied to input o_v = [1,0]
forty_five_rotation_theta = np.pi/4

# Rotating input vector o_v by 45 degrees
forty_five_rotation_v = rotate_2d_matrix(o_v, forty_five_rotation_theta)

fig, (ax1, ax2, ax3) = plt.subplots(1,3)

ax1.quiver(0, 0, zero_rotation_v[0], zero_rotation_v[1], angles='xy', scale_units='xy', scale=1, label='Original Vec=[1,0] with zero degree rotation', color='red')
ax1.set_xlim(-2,2)
ax1.set_ylim(-2,2)
ax1.grid()
ax1.legend()

ax2.quiver(0, 0, ninety_rotation_v[0], ninety_rotation_v[1], angles='xy', scale_units='xy', scale=1, label='Original Vec=[1,0] with 90 degree rotation', color='green')
ax2.set_xlim(-2,2)
ax2.set_ylim(-2,2)
ax2.grid()
ax2.legend()

ax3.quiver(0, 0, forty_five_rotation_v[0], forty_five_rotation_v[1], angles='xy', scale_units='xy', scale=1, label='Original Vec=[1,0] with 45 degree rotation',color='blue')
ax3.set_xlim(-2,2)
ax3.set_ylim(-2,2)
ax3.grid()
ax3.legend()

plt.show()