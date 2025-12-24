from unittest import skip

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#some clean up
df = yf.download('SPY', start='2018-01-01', end='2025-12-23')
df.to_csv('SPY.csv')


df = pd.read_csv('SPY.csv')

df = df.drop(index=[0, 1])
df = df.reset_index(drop=True)
df.to_csv('SPY.csv', index=False)

df = pd.read_csv('SPY.csv')

df = df.rename(columns={'Price': 'Date'})

#simple time-series plot
"""
df.set_index('Date', inplace=True)
plt.plot(df.index, df['Close'])
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('SPY Time Series')
plt.show()"""

#setting up the ma
short_window = 30
long_window = 120

df['MA_short'] = df['Close'].rolling(window=short_window).mean()
df['MA_long'] = df['Close'].rolling(window=long_window).mean()
df.to_csv('SPY.csv', index=False)

#if the mean of the short ma window higher than the long, we go long, else we stall
df['Signal'] = 0
df.loc[df['MA_short'] > df['MA_long'], 'Signal'] = 1

#avoiding look-ahead by shifting the signal by 1 day
df['Position'] = df['Signal'].shift(1)
df.to_csv('SPY.csv', index=False)