import yfinance as yf

tickers = ['AAPL', 'MSFT', 'GOOGL', 'NVDA', 'AMZN', 'META']
number_of_stocks = len(tickers)

stocks_full_csv = yf.download(tickers, start='2024-01-02', end='2025-11-01')

stocks = stocks_full_csv.Close
stocks.to_csv(r'data/stock_data_csv')
