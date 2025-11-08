import pandas as pd
import numpy as np
from stock_data_frames import stocks, number_of_stocks
from Sharpe_Ratio import sharpe

#Log returns, linearize in time
log_returns = np.log(1+stocks.pct_change())
avg_returns = log_returns.mean()

#calculate covariance matrix
cov_matrix = log_returns.cov() * 252

num_of_sims = 2500
#run monte carlo
sims = pd.DataFrame({'Weights': [],
                     'Sharpe Ratio': [],
                     'Exp Return': [],
                     'Volatility': []})


for i in range(num_of_sims):
    #random weights for stocks
    weights = np.array(np.random.random(number_of_stocks))
    #normalize
    weights = weights / weights.sum()

    #returns
    expected_annual_returns = np.sum((avg_returns * weights) * 252)

    #vol calculation
    volatility = np.sqrt(
    np.dot(
        weights.T, np.dot(cov_matrix, weights))
    )

    sims = pd.concat([sims, pd.DataFrame({'Weights': [weights], 
                                'Sharpe Ratio': [sharpe(expected_annual_returns, volatility)], 
                                'Exp Return': [expected_annual_returns],
                                'Volatility': [volatility]})])

