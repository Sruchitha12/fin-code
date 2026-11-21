
# EXPERIMENT 16
# Testing Lognormal Distribution of Stock Prices using Historical Data

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from scipy.stats import shapiro

# Stock symbol
stock = "RELIANCE.NS"

# Download historical stock prices
data = yf.download(
    stock,
    period="1y",
    auto_adjust=True
)

# Extract closing prices
prices = data["Close"].squeeze()

# Calculate logarithmic returns
log_returns = np.log(
    prices / prices.shift(1)
).dropna()

# Perform Shapiro-Wilk normality test
sample = log_returns.sample(
    min(5000, len(log_returns)),
    random_state=42
)

statistic, p_value = shapiro(sample)

# Display results
print("Shapiro-Wilk Test Statistic:", statistic)
print("P-value:", p_value)

# Interpret the result
if p_value > 0.05:
    print("Log returns approximately follow a normal distribution.")
    print("Stock prices are consistent with a lognormal model.")
else:
    print("Log returns do not follow a normal distribution.")
    print("Lognormal model is not supported by this test.")

# Plot histogram of log returns
plt.hist(log_returns, bins=30, density=True)

plt.title("Distribution of Stock Log Returns")
plt.xlabel("Log Returns")
plt.ylabel("Density")
plt.grid()
plt.show()
