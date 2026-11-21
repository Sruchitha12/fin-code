
# EXPERIMENT 3
# American Call and Put Option Pricing using Binomial Model

import numpy as np

# Input values
S0 = 100       # Initial stock price
K = 100        # Strike price
u = 1.2        # Upward multiplier
d = 0.8        # Downward multiplier
r = 0.05       # Risk-free interest rate per period
N = 3          # Number of periods

# Calculate risk-neutral probability
p = (1 + r - d) / (u - d)

# Generate stock prices at maturity
stock_prices = np.array([
    S0 * (u ** j) * (d ** (N - j))
    for j in range(N + 1)
])

# Calculate call and put payoffs at maturity
call_values = np.maximum(stock_prices - K, 0)
put_values = np.maximum(K - stock_prices, 0)

# Work backwards through the binomial tree
for i in range(N - 1, -1, -1):

    # Calculate stock prices at the current time step
    stock_prices = np.array([
        S0 * (u ** j) * (d ** (i - j))
        for j in range(i + 1)
    ])

    # Calculate continuation values
    call_continuation = (
        p * call_values[1:] +
        (1 - p) * call_values[:-1]
    ) / (1 + r)

    put_continuation = (
        p * put_values[1:] +
        (1 - p) * put_values[:-1]
    ) / (1 + r)

    # Calculate immediate exercise values
    call_exercise = np.maximum(stock_prices - K, 0)
    put_exercise = np.maximum(K - stock_prices, 0)

    # Choose the maximum value
    call_values = np.maximum(
        call_exercise, call_continuation
    )

    put_values = np.maximum(
        put_exercise, put_continuation
    )

# Display results
print("Risk-neutral probability:", p)
print("American Call Option Price:", call_values[0])
print("American Put Option Price:", put_values[0])
