
# EXPERIMENT 4
# Simulation of a Path of Scaled Symmetric Random Walk

import numpy as np
import matplotlib.pyplot as plt

# Input
N = 1000

# Generate random movements: +1 or -1
steps = np.random.choice([-1, 1], size=N)

# Calculate cumulative sum of movements
random_walk = np.cumsum(steps)

# Scale the random walk
scaled_walk = random_walk / np.sqrt(N)

# Generate time points
time = np.arange(N + 1) / N

# Include initial value zero
scaled_walk = np.insert(scaled_walk, 0, 0)

# Plot the scaled random walk
plt.plot(time, scaled_walk)

plt.title("Scaled Symmetric Random Walk")
plt.xlabel("Time")
plt.ylabel("W(N)(t)")
plt.grid()

plt.show()
