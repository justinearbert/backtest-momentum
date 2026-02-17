import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


ticker = "SPY"
data = yf.download("SPY", period="10y", interval="1d", auto_adjust=True)


# 2. Compute Moving Averages

data['MA50'] = data['Close'].rolling(window=50).mean()
data['MA200'] = data['Close'].rolling(window=200).mean()


# 3. Generate Signals

data['Signal'] = 0
data.loc[data['MA50'] > data['MA200'], 'Signal'] = 1
data.loc[data['MA50'] < data['MA200'], 'Signal'] = 0

# Shift to avoid look-ahead bias
data['Position'] = data['Signal'].shift(1)


# 4. Compute Returns

data['Market_Return'] = data['Close'].pct_change()
data['Strategy_Return'] = data['Market_Return'] * data['Position']


# 5. Cumulative Performance

data['Cumulative_Market'] = (1 + data['Market_Return']).cumprod()
data['Cumulative_Strategy'] = (1 + data['Strategy_Return']).cumprod()


# 6. Performance Metrics

def annualized_return(series):
    return (series.iloc[-1]) ** (252/len(series)) - 1

def annualized_vol(series):
    return series.std() * np.sqrt(252)

def sharpe_ratio(series):
    return annualized_return((1+series).cumprod()) / annualized_vol(series)

strategy_ann_return = annualized_return(data['Cumulative_Strategy'].dropna())
strategy_vol = annualized_vol(data['Strategy_Return'].dropna())
strategy_sharpe = sharpe_ratio(data['Strategy_Return'].dropna())

print("Strategy Annual Return:", round(strategy_ann_return, 4))
print("Strategy Annual Volatility:", round(strategy_vol, 4))
print("Strategy Sharpe Ratio:", round(strategy_sharpe, 4))


# 7. Plot Results

plt.figure(figsize=(12,6))
plt.plot(data['Cumulative_Market'], label="Buy & Hold")
plt.plot(data['Cumulative_Strategy'], label="50/200 Momentum Strategy")
plt.legend()
plt.title("SPY Momentum Strategy Backtest (50/200)")
plt.xlabel("Date", fontsize=12)
plt.ylabel("Cumulative Returns", fontsize=12)
plt.show()
