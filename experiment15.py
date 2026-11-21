
# EXPERIMENT 15
# Estimating Sharpe and Sortino Ratios for Stocks and Portfolio

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

# Risk-free annual interest rate
rf = 0.05

# Calculate daily risk-free rate
daily_rf = rf / 252

# Calculate Sharpe and Sortino ratios
for stock in stocks:

    # Calculate daily excess returns
    excess_returns = returns[stock] - daily_rf

    # Calculate Sharpe ratio
    sharpe = (
        excess_returns.mean() /
        returns[stock].std()
    ) * np.sqrt(252)

    # Calculate downside deviation
    downside = np.minimum(excess_returns, 0)

    downside_deviation = np.sqrt(
        np.mean(downside**2)
    )

    # Calculate Sortino ratio
    sortino = (
        excess_returns.mean() /
        downside_deviation
    ) * np.sqrt(252)

    print("\nStock:", stock)
    print("Sharpe Ratio:", sharpe)
    print("Sortino Ratio:", sortino)

# Calculate portfolio returns
weights = np.array([1/3, 1/3, 1/3])

portfolio_returns = returns @ weights

# Calculate portfolio excess returns
portfolio_excess = portfolio_returns - daily_rf

# Portfolio Sharpe ratio
portfolio_sharpe = (
    portfolio_excess.mean() /
    portfolio_returns.std()
) * np.sqrt(252)

# Portfolio downside deviation
portfolio_downside = np.minimum(
    portfolio_excess, 0
)

portfolio_downside_deviation = np.sqrt(
    np.mean(portfolio_downside**2)
)

# Portfolio Sortino ratio
portfolio_sortino = (
    portfolio_excess.mean() /
    portfolio_downside_deviation
) * np.sqrt(252)

print("\nPortfolio Sharpe Ratio:", portfolio_sharpe)
print("Portfolio Sortino Ratio:", portfolio_sortino)
