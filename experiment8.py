
# EXPERIMENT 8
# European Call and Put Pricing under GBM using Monte Carlo

import numpy as np

# Input values
S0 = 100
K = 100
r = 0.05
mu = 0.10
sigma = 0.20
T = 1
M = 100000

# Generate random normal values
Z = np.random.normal(0, 1, M)

# Simulate stock prices at maturity
ST = S0 * np.exp(
    (mu - 0.5 * sigma**2) * T
    + sigma * np.sqrt(T) * Z
)

# Calculate call payoffs
call_payoff = np.maximum(ST - K, 0)

# Calculate put payoffs
put_payoff = np.maximum(K - ST, 0)

# Calculate option prices
call_price = np.exp(-r * T) * np.mean(call_payoff)
put_price = np.exp(-r * T) * np.mean(put_payoff)

# Display results
print("European Call Option Price:", call_price)
print("European Put Option Price:", put_price)
