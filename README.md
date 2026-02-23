# Momentum Strategy Backtest

## Project Overview
Python script to backtest a 50/200 moving average momentum strategy on SPY (S&P 500 ETF) over the last 10 years.  
The strategy buys when the 50-day mean crosses above the 200-day mean and sells otherwise.

## Objective
To evaluate the performance of a simple momentum strategy compared to a buy & hold strategy.

## Materials Used
- Python  
- pandas  
- NumPy  
- yfinance  
- Matplotlib

## Key Features
- Computes 50-day and 200-day moving averages  
- Generates buy/sell signals based on MA crossovers  
- Calculates strategy returns, cumulative returns, and performance metrics (annualized return, volatility, Sharpe ratio)  
- Create plots on the cumulative performance vs buy & hold

# Output 
Strategy Annual Return: ...
Strategy Annual Volatility: ...
Strategy Sharpe Ratio: ...
