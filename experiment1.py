
import numpy as np
import matplotlib.pyplot as plt
from itertools import product

# Input values
S0 = 100
u = 1.2
d = 0.8
N = 3

# Generate all possible paths
paths = list(product(['U', 'D'], repeat=N))

# Calculate stock prices
all_prices = []

for path in paths:
    prices = [S0]

    for move in path:
        if move == 'U':
            new_price = prices[-1] * u
        else:
            new_price = prices[-1] * d

        prices.append(new_price)

    all_prices.append(prices)

# Display results
print("All possible stock price paths:")

for prices in all_prices:
    print(prices)

# Plot stock price paths
plt.figure(figsize=(8, 5))

for prices in all_prices:
    plt.plot(range(N + 1), prices, marker='o')

plt.xlabel("Period")
plt.ylabel("Stock Price")
plt.title("N-Period Binomial Stock Price Model")
plt.grid(True)
plt.show()




# EXPERIMENT 1
# Simulation of N-Period Binomial Model for Stock Prices

import numpy as np
import matplotlib.pyplot as plt
from itertools import product

# Input values
S0 = 100
u = 1.2
d = 0.8
N = 3

# Generate all possible paths
paths = list(product(['U', 'D'], repeat=N))

# Calculate stock prices
all_prices = []

for path in paths:
    prices = [S0]

    for move in path:
        if move == 'U':
            new_price = prices[-1] * u
        else:
            new_price = prices[-1] * d

        prices.append(new_price)

    all_prices.append(prices)

# Display results
print("All possible stock price paths:")

for prices in all_prices:
    print(prices)

# Plot stock price paths
plt.figure(figsize=(8, 5))

for prices in all_prices:
    plt.plot(range(N + 1), prices, marker='o')

plt.xlabel("Period")
plt.ylabel("Stock Price")
plt.title("N-Period Binomial Stock Price Model")
plt.grid(True)
plt.show()
