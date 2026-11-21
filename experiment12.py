
# EXPERIMENT 12
# Estimating Returns and Volatilities of Stocks and Portfolio

import numpy as np
import pandas as pd
import yfinance as yf

# Stock symbols
stocks = ["RELIANCE.NS", "TCS.NS", "INFY.NS"]

# Download historical stock prices
data = yf.download(
    stocks,
    period="1y",
    auto_adjust=True
)["Close"]

# Calculate daily returns
returns = data.pct_change().dropna()

# Calculate annualized returns
annual_returns = returns.mean() * 252

# Calculate annualized volatility
annual_volatility = returns.std() * np.sqrt(252)

# Create portfolio with equal weights
weights = np.array([1/3, 1/3, 1/3])

# Calculate portfolio daily returns
portfolio_returns = returns @ weights

# Calculate portfolio annualized return
portfolio_return = portfolio_returns.mean() * 252

# Calculate portfolio annualized volatility
portfolio_volatility = portfolio_returns.std() * np.sqrt(252)

# Display results
print("Individual Stock Annual Returns:")
print(annual_returns)

print("\nIndividual Stock Annual Volatilities:")
print(annual_volatility)

print("\nPortfolio Annual Return:", portfolio_return)
print("Portfolio Annual Volatility:", portfolio_volatility)
