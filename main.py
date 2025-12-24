import yfinance as yf
import pandas as pd

#df = yf.download('SPY', start='2018-01-01', end='2025-12-23')
#df.to_csv('SPY.csv')

df = pd.read_csv('SPY.csv')


print(df.head())