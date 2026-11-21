
# EXPERIMENT 11
# European Call and Put Pricing using Finite Difference Method

import numpy as np
import matplotlib.pyplot as plt

# Input values
S0 = 100
K = 100
r = 0.05
sigma = 0.2
T = 1

# Number of stock price and time steps
N = 200
M = 10000

# Calculate grid sizes
Smax = 3 * K
dS = Smax / N
dt = T / M

# Generate stock price grid
S = np.linspace(0, Smax, N + 1)

# Terminal payoff for call and put
call = np.maximum(S - K, 0)
put = np.maximum(K - S, 0)

# Calculate coefficients
i = np.arange(1, N)

a = 0.5 * dt * (sigma**2 * i**2 - r * i)
b = 1 - dt * (sigma**2 * i**2 + r)
c = 0.5 * dt * (sigma**2 * i**2 + r * i)

# Backward time calculation
for j in range(M):

    # Call option boundary conditions
    call[0] = 0
    call[-1] = Smax - K * np.exp(-r * (j + 1) * dt)

    # Put option boundary conditions
    put[0] = K * np.exp(-r * (j + 1) * dt)
    put[-1] = 0

    # Calculate new option values
    call_new = call.copy()
    put_new = put.copy()

    call_new[1:N] = (
        a * call[:-2] +
        b * call[1:-1] +
        c * call[2:]
    )

    put_new[1:N] = (
        a * put[:-2] +
        b * put[1:-1] +
        c * put[2:]
    )

    call = call_new
    put = put_new

# Find option prices at initial stock price
call_price = np.interp(S0, S, call)
put_price = np.interp(S0, S, put)

# Display results
print("European Call Option Price:", call_price)
print("European Put Option Price:", put_price)

# Plot option prices
plt.plot(S, call, label="Call Option")
plt.plot(S, put, label="Put Option")
plt.xlabel("Stock Price")
plt.ylabel("Option Price")
plt.title("Option Pricing using Finite Difference Method")
plt.legend()
plt.grid()
plt.show()
