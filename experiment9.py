
# EXPERIMENT 9
# Monte Carlo Pricing of Basket Options

import numpy as np

# Input values
S0 = np.array([100, 150, 200])
K = 150
r = 0.05
T = 1
M = 100000

# Volatility of each stock
sigma = np.array([0.2, 0.25, 0.3])

# Weights of stocks in the basket
weights = np.array([1/3, 1/3, 1/3])

# Correlation matrix
corr = np.array([
    [1.0, 0.5, 0.3],
    [0.5, 1.0, 0.4],
    [0.3, 0.4, 1.0]
])

# Cholesky decomposition
L = np.linalg.cholesky(corr)

# Generate independent random values
Z = np.random.normal(0, 1, (M, 3))

# Generate correlated random values
Z_corr = Z @ L.T

# Simulate stock prices at maturity
ST = S0 * np.exp(
    (r - 0.5 * sigma**2) * T
    + sigma * np.sqrt(T) * Z_corr
)

# Calculate basket value
basket = np.sum(ST * weights, axis=1)

# Calculate call and put payoffs
call_payoff = np.maximum(basket - K, 0)
put_payoff = np.maximum(K - basket, 0)

# Calculate option prices
call_price = np.exp(-r*T) * np.mean(call_payoff)
put_price = np.exp(-r*T) * np.mean(put_payoff)

# Display results
print("Basket Call Option Price:", call_price)
print("Basket Put Option Price:", put_price)
