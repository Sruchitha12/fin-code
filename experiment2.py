
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




# EXPERIMENT 2
# European Call and Put Option Pricing using N-Period Binomial Model

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

