from stock_data_frames import stocks, number_of_stocks
import pandas as pd
import numpy as np


#Log returns, linearize in time
log_returns = np.log(1+stocks.pct_change())
avg_returns = log_returns.mean()

#random weights for stocks
weights = np.array(np.random.random(number_of_stocks))
#normalize
weights = weights / weights.sum()

#returns
expected_annual_returns = np.sum((avg_returns * weights) * 252)

#calculate volatility
cov_matrix = log_returns.cov() * 252
variance = np.sqrt(
    np.dot(
        weights.T, np.dot(cov_matrix, weights)
    )
)

#calculate Sharpe ratio, using 1% as risk-free return
sharpe = (expected_annual_returns - 0.01) / variance
