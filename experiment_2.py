
# EXPERIMENT 2
# European Call and Put Option Pricing using Binomial Model

# Importing required library
import numpy as np

# Input values
S0 = 100       # Initial stock price
K = 100        # Strike price
u = 1.2        # Upward multiplier
d = 0.8        # Downward multiplier
r = 0.05       # Risk-free interest rate

# Calculate risk-neutral probability
p = (1 + r - d) / (u - d)

# Calculate stock prices
Su = S0 * u
Sd = S0 * d

# Calculate Call option payoffs
Cu = max(Su - K, 0)
Cd = max(Sd - K, 0)

# Calculate Put option payoffs
Pu = max(K - Su, 0)
Pd = max(K - Sd, 0)

# Calculate European Call price
Call = (p * Cu + (1 - p) * Cd) / (1 + r)

# Calculate European Put price
Put = (p * Pu + (1 - p) * Pd) / (1 + r)

# Display results
print("Risk-neutral probability:", p)
print("European Call Option Price:", Call)
print("European Put Option Price:", Put)
