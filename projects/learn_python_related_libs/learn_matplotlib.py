import matplotlib.pyplot as plt

# Basic Plot
x = [0,1,2,3,4,5]
y = [0,3,2,3,4,5]

fig, ax = plt.subplots(1, 1)
ax.set_title(label="My First Plot")
ax.set_xlabel("X - Axis")
ax.grid(visible=True)
ax.plot(x, y)
ax.set_xlim(0,5)
ax.set_ylim(0,5)
plt.show()
