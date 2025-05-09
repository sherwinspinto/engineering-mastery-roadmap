# Sample Python script to visualize sampling
import numpy as np
import matplotlib.pyplot as plt

# Continuous signal
t = np.linspace(0, 1, 1000)
y = np.sin(2 * np.pi * 5 * t)

# Sampled signal
ts = np.linspace(0, 1, 20)
ys = np.sin(2 * np.pi * 5 * ts)

plt.plot(t, y, label='Continuous')
plt.stem(ts, ys, linefmt='r-', markerfmt='ro', basefmt='r-', label='Sampled')
plt.legend()
plt.title('Sampling a Sine Wave')
plt.show()
