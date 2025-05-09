import numpy as np
import matplotlib.pyplot as plt

# Original continuous signal
t = np.linspace(0, 1, 1000)
freq = 5  # Hz
y = np.sin(2 * np.pi * freq * t)

# Proper sampling: meets Nyquist rate
fs_proper = 20  # samples/sec
ts_proper = np.linspace(0, 1, fs_proper)
ys_proper = np.sin(2 * np.pi * freq * ts_proper)

# Undersampling: causes aliasing
fs_alias = 8  # below Nyquist
ts_alias = np.linspace(0, 1, fs_alias)
ys_alias = np.sin(2 * np.pi * freq * ts_alias)

# Plotting
fig, axs = plt.subplots(2, 1, figsize=(10, 6))

# Proper Sampling Plot
axs[0].plot(t, y, label='Original (Continuous)', color='blue')
axs[0].stem(ts_proper, ys_proper, linefmt='r-', markerfmt='ro', basefmt='r-', label='Sampled (fs=20Hz)')
axs[0].set_title('Proper Sampling (fs = 20 Hz)')
axs[0].legend()
axs[0].grid(True)

# Aliased Sampling Plot
axs[1].plot(t, y, label='Original (Continuous)', color='blue')
axs[1].stem(ts_alias, ys_alias, linefmt='g-', markerfmt='go', basefmt='g-', label='Sampled (fs=8Hz)')
axs[1].set_title('Aliased Sampling (fs = 8 Hz)')
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()