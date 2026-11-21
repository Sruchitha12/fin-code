
# EXPERIMENT 14
# Estimating Alpha and Beta for Stocks and Portfolio

import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import linregress

# Stock symbols
stocks = ["RELIANCE.NS", "TCS.NS", "INFY.NS"]

# Download stock prices and market index
symbols = stocks + ["^NSEI"]

data = yf.download(
    symbols,
    period="1y",
    auto_adjust=True
)["Close"]

# Calculate daily returns
returns = data.pct_change().dropna()

# Extract market returns
market_returns = returns["^NSEI"]

# Calculate alpha and beta for each stock
for stock in stocks:

    result = linregress(
        market_returns,
        returns[stock]
    )

    alpha = result.intercept
    beta = result.slope

    print("\nStock:", stock)
    print("Alpha:", alpha)
    print("Beta:", beta)

# Calculate equal-weighted portfolio returns
weights = np.array([1/3, 1/3, 1/3])

portfolio_returns = returns[stocks] @ weights

# Calculate portfolio alpha and beta
result = linregress(
    market_returns,
    portfolio_returns
)

print("\nPortfolio Alpha:", result.intercept)
print("Portfolio Beta:", result.slope)
