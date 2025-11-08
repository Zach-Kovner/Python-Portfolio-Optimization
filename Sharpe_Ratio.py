from stock_data_frames import stocks

def sharpe(expected_annual_returns, variance):
    return (expected_annual_returns - 0.01) / variance
