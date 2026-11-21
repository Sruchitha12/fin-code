
# EXPERIMENT 6
# Simulation of Stock Price Process Driven by Brownian Motion

import numpy as np
import matplotlib.pyplot as plt

# Input values
S0 = 100
mu = 0.10
sigma = 0.20
T = 1
N = 1000

# Calculate time interval
dt = T / N

# Generate random normal values
Z = np.random.normal(0, 1, N)

# Create stock price array
S = np.zeros(N + 1)
S[0] = S0

# Calculate stock prices
for i in range(N):
    S[i + 1] = S[i] * np.exp(
        (mu - 0.5 * sigma**2) * dt
        + sigma * np.sqrt(dt) * Z[i]
    )

# Generate time points
time = np.linspace(0, T, N + 1)

# Plot stock price path
plt.plot(time, S)
plt.title("Stock Price Process Driven by Brownian Motion")
plt.xlabel("Time")
plt.ylabel("Stock Price")
plt.grid()
plt.show()
