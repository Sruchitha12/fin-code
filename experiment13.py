
# EXPERIMENT 13
# Short, Medium and Long Moving Averages

import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

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

# Calculate moving averages
short_ma = prices.rolling(window=20).mean()
medium_ma = prices.rolling(window=50).mean()
long_ma = prices.rolling(window=200).mean()

# Plot stock price and moving averages
plt.figure(figsize=(12, 6))

plt.plot(prices, label="Stock Price")
plt.plot(short_ma, label="Short MA (20 days)")
plt.plot(medium_ma, label="Medium MA (50 days)")
plt.plot(long_ma, label="Long MA (200 days)")

plt.title("Moving Averages of Stock Prices")
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.legend()
plt.grid()
plt.show()
