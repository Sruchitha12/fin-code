
# EXPERIMENT 5
# Simulation of a Path of Brownian Motion

import numpy as np
import matplotlib.pyplot as plt

# Input
T = 1
N = 1000

# Calculate time interval
dt = T / N

# Generate random normal values
Z = np.random.normal(0, 1, N)

# Calculate Brownian motion increments
dW = np.sqrt(dt) * Z

# Calculate Brownian motion path
W = np.cumsum(dW)

# Generate time points
time = np.linspace(0, T, N + 1)

# Include initial value zero
W = np.insert(W, 0, 0)

# Plot Brownian motion
plt.plot(time, W)

plt.title("Simulation of Brownian Motion")
plt.xlabel("Time")
plt.ylabel("W(t)")
plt.grid()

plt.show()
