### INF601 - Advanced Programming in Python
### Justin Stewart
### Mini Project 1

import pprint
import yfinance as yf
msft = yf.Ticker("MSFT")

mytickers = ["AMD", "INTC", "NVDA", "AMC", "GME"]
mydata = {}

for ticker in mytickers:
    result = yf.Ticker(ticker)
    mydata[ticker] = {'Ticker': ticker,
                      'dailyHigh': result.info['dayHigh']}

pprint.pprint(mydata)

hist = msft.history(period="1mo")

ten_days = hist.iloc[-10:]

pprint.pprint(ten_days)