import yfinance as yf
import pandas as pd

t = yf.Ticker('AAPL')
dati = t.history(period = '10Y')

dati.to_csv('AzioniApple10Anni')
print('FATTO!')
print(dati.head())