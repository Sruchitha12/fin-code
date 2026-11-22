
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


# EXPERIMENT 2
# European Call and Put Option Pricing using N-Period Binomial Model

# Importing required library
import numpy as np

# Input values
S0 = 100
K = 100
u = 1.2
d = 0.8
r = 0.05
N = 3

# Calculate risk-neutral probability
p = (1 + r - d) / (u - d)

# Calculate option payoffs at final period
call = []
put = []

for i in range(N + 1):
    S = S0 * (u ** (N - i)) * (d ** i)

    call.append(max(S - K, 0))
    put.append(max(K - S, 0))

# Calculate option prices backwards
for j in range(N):
    new_call = []
    new_put = []

    for i in range(len(call) - 1):
        new_call.append(
            (p * call[i] + (1 - p) * call[i + 1]) / (1 + r)
        )

        new_put.append(
            (p * put[i] + (1 - p) * put[i + 1]) / (1 + r)
        )

    call = new_call
    put = new_put

# Display results
print("Risk-neutral probability:", p)
print("European Call Option Price:", call[0])
print("European Put Option Price:", put[0])

