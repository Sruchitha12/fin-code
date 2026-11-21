
# EXPERIMENT 10
# European Call and Put Pricing under Heston Model using Monte Carlo

import numpy as np

# Input values
S0 = 100
K = 100
r = 0.05
T = 1

# Heston model parameters
v0 = 0.04
kappa = 2
theta = 0.04
xi = 0.3
rho = -0.7

# Simulation parameters
N = 252
M = 20000

# Calculate time interval
dt = T / N

# Initialize stock prices and variance
S = np.full(M, S0)
v = np.full(M, v0)

# Simulate stock prices and variance
for i in range(N):

    # Generate independent random values
    Z1 = np.random.normal(0, 1, M)
    Z2 = np.random.normal(0, 1, M)

    # Generate correlated random values
    Z2_corr = rho * Z1 + np.sqrt(1-rho**2) * Z2

    # Update stock prices
    S = S * np.exp(
        (r - 0.5 * v) * dt
        + np.sqrt(v * dt) * Z1
    )

    # Update variance
    v = np.maximum(
        v + kappa * (theta-v) * dt
        + xi * np.sqrt(v * dt) * Z2_corr,
        0
    )

# Calculate call and put payoffs
call_payoff = np.maximum(S-K, 0)
put_payoff = np.maximum(K-S, 0)

# Calculate option prices
call_price = np.exp(-r*T) * np.mean(call_payoff)
put_price = np.exp(-r*T) * np.mean(put_payoff)

# Display results
print("European Call Option Price:", call_price)
print("European Put Option Price:", put_price)
