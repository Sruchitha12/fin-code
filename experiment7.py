
# EXPERIMENT 7
# Simulation of Uncorrelated and Correlated Brownian Motions

import numpy as np
import matplotlib.pyplot as plt

# Input values
T = 1
N = 1000
rho = 0.8

# Calculate time interval
dt = T / N

# Generate independent random normal values
Z1 = np.random.normal(0, 1, N)
Z2 = np.random.normal(0, 1, N)

# Generate uncorrelated Brownian motions
dW1 = np.sqrt(dt) * Z1
dW2 = np.sqrt(dt) * Z2

W1 = np.cumsum(dW1)
W2 = np.cumsum(dW2)

# Generate correlated Brownian motions
dW3 = np.sqrt(dt) * Z1
dW4 = np.sqrt(dt) * (
    rho * Z1 + np.sqrt(1 - rho**2) * Z2
)

W3 = np.cumsum(dW3)
W4 = np.cumsum(dW4)

# Generate time points
time = np.linspace(0, T, N + 1)

# Add initial zero
W1 = np.insert(W1, 0, 0)
W2 = np.insert(W2, 0, 0)
W3 = np.insert(W3, 0, 0)
W4 = np.insert(W4, 0, 0)

# Plot uncorrelated Brownian motions
plt.figure(figsize=(10, 4))
plt.plot(time, W1, label="W1")
plt.plot(time, W2, label="W2")
plt.title("Uncorrelated Brownian Motions")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.grid()
plt.show()

# Plot correlated Brownian motions
plt.figure(figsize=(10, 4))
plt.plot(time, W3, label="W3")
plt.plot(time, W4, label="W4")
plt.title("Correlated Brownian Motions")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.grid()
plt.show()
